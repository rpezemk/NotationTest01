import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QToolBar, QAction
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QBrush, QPen, QColor

class NoteControl(QGraphicsEllipseItem):
    def __init__(self, rect, *args, **kwargs):
        super().__init__(rect, *args, **kwargs)
        self.setBrush(QBrush(QColor("red")))
        self.setPen(QPen(Qt.NoPen))
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable)
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.setAcceptedMouseButtons(Qt.LeftButton)

    def mousePressEvent(self, event):
        # Change color on click
        current_color = self.brush().color()
        new_color = QColor("blue") if current_color == QColor("red") else QColor("red")
        self.setBrush(QBrush(new_color))
        # Call base class method
        super().mousePressEvent(event)