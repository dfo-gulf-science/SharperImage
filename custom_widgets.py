from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QWheelEvent, QPainter
from PySide6.QtWidgets import QLabel, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem


class ZoomableGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: black")

        # Create a scene (the canvas) and assign it to the view
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # This item will hold our actual image
        self.pixmap_item = QGraphicsPixmapItem()
        self.scene.addItem(self.pixmap_item)

        # UI Styling & Performance optimizations
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)  # Keeps image crisp
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)  # <-- THE MAGIC LINE
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag) # allows dragging

        # Hide scrollbars if you want a clean borderless look
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def setImage(self, pixmap):
        """Loads an image into the view and resets the scale."""
        if not pixmap.isNull():
            self.pixmap_item.setPixmap(pixmap)
            # Reset any previous zoom transformations
            self.resetTransform()
            # Fit the scene boundaries exactly to the image size
            self.setSceneRect(self.pixmap_item.boundingRect())

    def wheelEvent(self, event: QWheelEvent):
        # Check if Control key is held down
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            # Determine zoom scale factor
            zoom_factor = 1.15 if event.angleDelta().y() > 0 else 1.0 / 1.15

            # Apply the scale. Because AnchorUnderMouse is enabled,
            # Qt handles all the complex math to keep the cursor locked to the image pixel!
            self.scale(zoom_factor, zoom_factor)

            event.accept()
        else:
            # Let standard scrolling pass through if Ctrl isn't held
            super().wheelEvent(event)
