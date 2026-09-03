import os.path
import sys

from PySide6.QtCore import Qt, QSize, QSettings
from PySide6.QtGui import QPixmap, QTransform, QResizeEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QFileDialog, QMessageBox
# Import the generated layout class from your compiled file
from ui_main_window import Ui_MainWindow
import cv2

from utils import sharpen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # Instantiate the generated UI layout class
        self.ui = Ui_MainWindow()
        # Cleanly inject the layouts and widgets straight into this instance
        self.ui.setupUi(self)

        self.setWindowTitle("The Sharper Image")

        # instantiate settings
        self.settings = QSettings("DFO", "TheSharperImage")

        # see if we should load some defaults for directories
        last_source_dir = self.settings.value("last_source_dir", "")
        last_target_dir = self.settings.value("last_target_dir", "")
        last_sigma = self.settings.value("last_sigma", 2)
        last_amount = self.settings.value("last_amount", 17)

        self.ui.sourceDir.setText(last_source_dir)
        self.ui.targetDir.setText(last_target_dir)
        self.ui.sigmaSlider.setValue(int(last_sigma))
        self.ui.amountSlider.setValue(int(last_amount))

        # set the slider values into the appropriate text boxes
        self.ui.sigmaDisplay.setText(str(self.ui.sigmaSlider.value()))
        self.ui.sigmaSlider.valueChanged.connect(self.update_sigma_display)
        self.ui.sigmaDisplay.editingFinished.connect(self.validate_sigma_text)

        self.ui.amountDisplay.setText(str(self.ui.amountSlider.value()))
        self.ui.amountSlider.valueChanged.connect(self.update_amount_display)
        self.ui.amountDisplay.editingFinished.connect(self.validate_amount_text)

        # insert the original otolith pic into the appropriate label widget
        self.original_filename = "original_otolith.tif"
        original_pixmap = QPixmap(self.original_filename)
        original_pixmap = original_pixmap.scaled(
            QSize(500, 500),
            aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
            mode=Qt.TransformationMode.SmoothTransformation  # Keeps the image crisp
        )
        self.ui.originalImage.setPixmap(original_pixmap)

        # now we need the transformation with the defaulted values
        self.update_image()

        # connect the buttons with file pickers
        self.ui.sourceFileBrowse.clicked.connect(self.open_source_dir_picker)
        self.ui.targetFileBrowse.clicked.connect(self.open_target_dir_picker)

        # connect the action exit menu action
        self.ui.actionExit.triggered.connect(self.close)

        # control behaviour of ok button
        self.ui.proceedButton.clicked.connect(self.validate_and_submit)

        # prime the progress bar
        self.ui.progressBar.setValue(0)

    def validate_and_submit(self):
        # make all the fields disabled
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
        self.settings.setValue("last_source_dir", source_dir)
        self.settings.setValue("last_target_dir", target_dir)

        self.close()






    def disable_controls(self, value):
        self.ui.sourceDir.setDisabled(value)
        self.ui.targetDir.setDisabled(value)
        self.ui.sigmaSlider.setDisabled(value)
        self.ui.sigmaDisplay.setDisabled(value)
        self.ui.amountSlider.setDisabled(value)
        self.ui.amountDisplay.setDisabled(value)

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
        self.settings.setValue("last_sigma", str(value))


    def update_amount_display(self, value):
        self.ui.amountDisplay.setText(str(value))
        self.update_image()
        self.settings.setValue("last_amount", str(value))

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

        # 1. Compress the OpenCV BGR array into a JPG/PNG memory buffer
        _, buffer = cv2.imencode('.png', new_data)

        # 2. Load the raw bytes straight into PySide without touching the disk
        new_pixmap = QPixmap()
        new_pixmap.loadFromData(buffer.tobytes())
        new_pixmap = new_pixmap.scaled(
            QSize(500, 500),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation  # Keeps the image crisp
        )

        self.ui.newImage.setPixmap(new_pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
