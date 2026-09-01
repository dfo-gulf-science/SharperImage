import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
# Import the generated layout class from your compiled file
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Instantiate the generated UI layout class
        self.ui = Ui_MainWindow()
        # Cleanly inject the layouts and widgets straight into this instance
        self.ui.setupUi(self)

        self.setWindowTitle("The Sharper Image")

        # Load your original image
        original_pixmap = QPixmap("oto.png")

        # 1. Convert to a QImage
        image = original_pixmap.toImage()

        # 2. Mirror the image
        # Parameters: mirrored(horizontal: bool, vertical: bool)
        flipped_image = image.mirrored(True, False)  # Flips horizontally (mirror effect)

        # 3. Convert back to QPixmap for display
        flipped_pixmap = QPixmap.fromImage(flipped_image)

        self.ui.title_image_1.setPixmap(original_pixmap)
        self.ui.title_image_2.setPixmap(flipped_pixmap)

    def handle_click(self):
        print("Button clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
