from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QWheelEvent
from PySide6.QtWidgets import QLabel


class ZoomableLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.original_pixmap = QPixmap()
        self.zoom_factor = 1.0
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add a helper function to set the image later in your code
    def setImage(self, pixmap):
        self.original_pixmap = pixmap
        self.zoom_factor = 1.0
        self.update_image()

    def wheelEvent(self, event: QWheelEvent):
        # Check if the Control key is currently held down
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            # Determine scroll direction: event.angleDelta().y() > 0 means scrolling up
            if event.angleDelta().y() > 0:
                self.zoom_factor *= 1.15  # Zoom in by 15%
            else:
                self.zoom_factor /= 1.15  # Zoom out by 15%

            # Optional: Clamp the zoom so it doesn't get ridiculously small or large
            self.zoom_factor = max(0.1, min(self.zoom_factor, 10.0))

            self.update_image()
            event.accept()  # Tell Qt we handled this event
        else:
            # If Ctrl isn't held, let the standard wheel event happen (like scrolling a webpage)
            super().wheelEvent(event)

    def update_image(self):
        if not self.original_pixmap.isNull():
            # Calculate new dimensions
            new_width = int(self.original_pixmap.width() * self.zoom_factor)
            new_height = int(self.original_pixmap.height() * self.zoom_factor)

            # Scale the original image smoothly
            scaled_pixmap = self.original_pixmap.scaled(
                new_width,
                new_height,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation  # Keeps it crisp
            )
            self.setPixmap(scaled_pixmap)

