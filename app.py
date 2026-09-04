import os.path
import sys
import time

from PySide6.QtCore import Qt, QSize, QSettings, QCoreApplication
from PySide6.QtGui import QPixmap, QTransform, QResizeEvent, QWheelEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QFileDialog, QMessageBox
# Import the generated layout class from your compiled file
from ui_main_window import Ui_MainWindow
import cv2

from utils import sharpen, get_asset_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.is_cancelled = False

        # Instantiate the generated UI layout class
        self.ui = Ui_MainWindow()
        # Cleanly inject the layouts and widgets straight into this instance
        self.ui.setupUi(self)

        self.setWindowTitle("The Sharper Image")

        # instantiate settings
        self.settings = QSettings("DFO", "TheSharperImage")

        # initialize controls
        self.disable_controls(False)

        # initialize the options for the color map combobox
        options = [
            ("None", None),
            ("AUTUMN".title(), cv2.COLORMAP_AUTUMN),
            ("BONE".title(), cv2.COLORMAP_BONE),
            ("JET".title(), cv2.COLORMAP_JET),
            ("WINTER".title(), cv2.COLORMAP_WINTER),
            ("RAINBOW".title(), cv2.COLORMAP_RAINBOW),
            ("OCEAN".title(), cv2.COLORMAP_OCEAN),
            ("SUMMER".title(), cv2.COLORMAP_SUMMER),
            ("SPRING".title(), cv2.COLORMAP_SPRING),
            ("COOL".title(), cv2.COLORMAP_COOL),
            ("HSV", cv2.COLORMAP_HSV),
            ("PINK".title(), cv2.COLORMAP_PINK),
            ("HOT".title(), cv2.COLORMAP_HOT),
            ("PARULA".title(), cv2.COLORMAP_PARULA),
            ("MAGMA".title(), cv2.COLORMAP_MAGMA),
            ("INFERNO".title(), cv2.COLORMAP_INFERNO),
            ("PLASMA".title(), cv2.COLORMAP_PLASMA),
            ("VIRIDIS".title(), cv2.COLORMAP_VIRIDIS),
            ("CIVIDIS".title(), cv2.COLORMAP_CIVIDIS),
            ("TWILIGHT".title(), cv2.COLORMAP_TWILIGHT),
            ("TWILIGHT_SHIFTED".title(), cv2.COLORMAP_TWILIGHT_SHIFTED),
            ("TURBO".title(), cv2.COLORMAP_TURBO),
            ("DEEPGREEN".title(), cv2.COLORMAP_DEEPGREEN),
        ]
        for label, value in options:
            self.ui.colorMap.addItem(label, value)
        self.ui.colorMap.currentIndexChanged.connect(self.update_image)

        self.load_defaults()

        # set the slider values into the appropriate text boxes
        self.ui.sigmaDisplay.setText(str(self.ui.sigmaSlider.value()))
        self.ui.sigmaSlider.valueChanged.connect(self.update_sigma_display)
        self.ui.sigmaDisplay.editingFinished.connect(self.validate_sigma_text)

        self.ui.amountDisplay.setText(str(self.ui.amountSlider.value()))
        self.ui.amountSlider.valueChanged.connect(self.update_amount_display)
        self.ui.amountDisplay.editingFinished.connect(self.validate_amount_text)

        # insert the original otolith pic into the appropriate label widget
        self.original_filename = get_asset_path("original_otolith.tif")
        original_pixmap = QPixmap(self.original_filename)
        original_pixmap = original_pixmap.scaled(
            QSize(500, 500),
            aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
            mode=Qt.TransformationMode.SmoothTransformation  # Keeps the image crisp
        )
        # self.ui.originalImage.setPixmap(original_pixmap)
        self.ui.originalImage.setImage(original_pixmap)
        # now we need the transformation with the defaulted values
        self.update_image()

        # connect the buttons with file pickers
        self.ui.sourceFileBrowse.clicked.connect(self.open_source_dir_picker)
        self.ui.targetFileBrowse.clicked.connect(self.open_target_dir_picker)

        # connect menu actions
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.open_about_dialog)
        self.ui.actionRestoreDefaults.triggered.connect(self.restore_defaults)

        # control behaviour of ok button
        self.ui.proceedButton.clicked.connect(self.validate_and_submit)
        self.ui.cancelButton.clicked.connect(self.cancel_processing)

        # prime the progress bar
        self.ui.progressBar.setValue(0)

    def cancel_processing(self):
        self.is_cancelled = True

    def load_defaults(self):
        # see if we should load some defaults for directories
        last_source_dir = self.settings.value("last_source_dir", "")
        last_target_dir = self.settings.value("last_target_dir", "")
        last_sigma = self.settings.value("last_sigma", 2)
        last_amount = self.settings.value("last_amount", 17)
        last_color_map = self.settings.value("last_color_map", None)

        self.ui.sourceDir.setText(last_source_dir)
        self.ui.targetDir.setText(last_target_dir)
        self.ui.sigmaSlider.setValue(int(last_sigma))
        self.ui.amountSlider.setValue(int(last_amount))
        color_map_idx = self.ui.colorMap.findData(last_color_map)
        if color_map_idx > -1:
            self.ui.colorMap.setCurrentIndex(color_map_idx)
        self.ui.status.setText("Ready.")

    def restore_defaults(self):
        self.settings.setValue("last_source_dir", "")
        self.settings.setValue("last_target_dir", "")
        self.settings.setValue("last_sigma", 2)
        self.settings.setValue("last_amount", 17)
        self.settings.setValue("last_color_map", None)
        self.load_defaults()

    def open_about_dialog(self):
        QMessageBox.information(self, "About this application", """
<span>
This application was created by Fisheries and Oceans Canada, Centre for Advice and Data Integration (CADI) of the Gulf Region.
<br>
<br>
The code repository is located at:  <a href='https://github.com/dfo-gulf-science/SharperImage'>https://github.com/dfo-gulf-science/SharperImage</a>.
</span>
""")

    def validate_and_submit(self):
        # make all the fields disabled
        self.is_cancelled = False
        self.disable_controls(True)

        source_dir = self.ui.sourceDir.text().strip()
        target_dir = self.ui.targetDir.text().strip()

        # some basic validation

        if not source_dir:
            QMessageBox.warning(self, "Validation Error", "The you need to have a source directory before continuing!")
            return
        elif not os.path.exists(source_dir):
            QMessageBox.warning(self, "Validation Error", "The source directory does not exist!")
            return
        elif not target_dir:
            QMessageBox.warning(self, "Validation Error", "The you need to have a target directory before continuing!")
            return
        elif not os.path.exists(target_dir):
            QMessageBox.warning(self, "Validation Error", "The target directory does not exist!")
            return

        # let's create a memory

        total_files = os.listdir(source_dir).__len__()
        idx = 0
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(total_files)
        self.ui.progressBar.setValue(0)
        self.update_file_status(0, total_files)
        sigma = self.ui.sigmaSlider.value()
        amount = self.ui.amountSlider.value()
        color_map = self.ui.colorMap.currentData()

        self.settings.setValue("last_source_dir", source_dir)
        self.settings.setValue("last_target_dir", target_dir)
        self.settings.setValue("last_color_map", color_map)
        self.settings.setValue("last_sigma", sigma)
        self.settings.setValue("last_amount", amount)

        for f in os.listdir(source_dir):
            og_path = os.path.join(source_dir, f)
            # we want to make sure we are not going to inadvertently overwrite the original file
            new_f = f.split(".")[0] + "-enhanced." + f.split(".")[-1]
            new_path = os.path.join(target_dir, new_f)
            img = cv2.imread(og_path)
            new_data = sharpen(img, sigma, amount)
            if color_map is not None:
                new_data = cv2.applyColorMap(new_data, color_map)
            cv2.imwrite(new_path, img=new_data)
            idx += 1
            self.update_file_status(idx, total_files)
            self.ui.progressBar.setValue(idx)
            QCoreApplication.processEvents()
            if self.is_cancelled:
                break

        if not self.is_cancelled:
            QMessageBox.information(self, "Job Successful", f"All {idx} images have been processed!")
        else:
            QMessageBox.warning(self, "Job Cancelled",
                                f"A total of {idx} images were processed before the job was cancelled.")
        self.ui.progressBar.setValue(0)
        self.ui.status.setText("Ready.")
        self.disable_controls(False)

    def update_file_status(self, current: int, total: int):
        txt = f"{current} of {total} files processed..."
        self.ui.status.setText(txt)

    def disable_controls(self, value):
        self.ui.sourceDir.setDisabled(value)
        self.ui.targetDir.setDisabled(value)
        self.ui.sigmaSlider.setDisabled(value)
        self.ui.sigmaDisplay.setDisabled(value)
        self.ui.amountSlider.setDisabled(value)
        self.ui.amountDisplay.setDisabled(value)
        self.ui.colorMap.setDisabled(value)
        self.ui.proceedButton.setDisabled(value)
        self.ui.cancelButton.setDisabled(not value)

    def open_source_dir_picker(self):
        # 4. Trigger the native file dialog when clicked
        path = QFileDialog.getExistingDirectory(self)
        if path:
            self.ui.sourceDir.setText(path)

    def open_target_dir_picker(self):
        # 4. Trigger the native file dialog when clicked
        path = QFileDialog.getExistingDirectory(self)
        if path:
            self.ui.targetDir.setText(path)

    def update_sigma_display(self, value):
        self.ui.sigmaDisplay.setText(str(value))
        self.update_image()

    def update_amount_display(self, value):
        self.ui.amountDisplay.setText(str(value))
        self.update_image()

    def validate_sigma_text(self):
        current_text = self.ui.sigmaDisplay.text()
        try:
            value = int(current_text)
        except ValueError:
            value = self.ui.sigmaSlider.minimum()
            self.ui.sigmaDisplay.setText(str(value))
        self.ui.sigmaSlider.setValue(value)

    def validate_amount_text(self):
        current_text = self.ui.amountDisplay.text()
        try:
            value = int(current_text)
        except ValueError:
            value = self.ui.amountSlider.minimum()
            self.ui.amountDisplay.setText(str(value))
        self.ui.amountSlider.setValue(value)

    def update_image(self):
        sigma = self.ui.sigmaSlider.value()
        amount = self.ui.amountSlider.value()
        original_data = cv2.imread(self.original_filename)
        new_data = sharpen(original_data, sigma, amount)
        color_map = self.ui.colorMap.currentData()
        if color_map is not None:
            new_data = cv2.applyColorMap(new_data, color_map)

        # 1. Compress the OpenCV BGR array into a JPG/PNG memory buffer
        _, buffer = cv2.imencode('.png', new_data)

        # 2. Load the raw bytes straight into PySide without touching the disk
        new_pixmap = QPixmap()
        new_pixmap.loadFromData(buffer.tobytes())
        new_pixmap = new_pixmap.scaled(
            QSize(500, 500),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.ui.newImage.setImage(new_pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
