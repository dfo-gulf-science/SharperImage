import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QTransform, QResizeEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
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


    def handle_click(self):
        print("Button clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
