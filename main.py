import random
import sys
from PyQt5.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem,
    QGraphicsRectItem, QMainWindow, QVBoxLayout, QHBoxLayout, 
    QPushButton, QWidget, QToolBar, QAction, QMenu, QMessageBox)

from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QBrush, QPen, QColor
from GUI.NoteControl import NoteControl

from Helpers.TestHelper import TestHelper
from Helpers.ActionHelper import ActionHelper
from test import CustomPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.toolBar: QToolBar = None
        self.setWindowTitle("PyQt5 Canvas with Clickable Items and Top Pane")
        self.create_menu()
        self.graphics_scene = QGraphicsScene(self)
        self.graphics_scene.setSceneRect(0, 0, 400, 300)
        self.graphics_view = QGraphicsView(self.graphics_scene, self)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.vertical_layout = QVBoxLayout(central_widget)
        self.vertical_layout.addWidget(self.toolBar)
        self.vertical_layout.addWidget(self.graphics_view)

    def create_menu(self) -> None:
        ActionHelper.AssignMenuEntry(self, self.open_method, "File", "Open" )
        ActionHelper.AssignMenuEntry(self, self.save_method, "File", "Save" )
        ActionHelper.AssignMenuEntry(self, self.close, "File", "Special..", "special close" )
        ActionHelper.AssignMenuEntry(self, self.close, "File", "Quit")
        ActionHelper.AssignMenuEntry(self, self.about, "Help", "About")
        ActionHelper.AssignToolbarEntry(self, self.close, "a", "b", "c")
        ActionHelper.AssignToolbarEntry(self, self.close, "a", "b", "d")
        
    def open_method(self):
        pass
    
    def save_method(self):
        pass
    
    def about(self):
        print("About action triggered")    

    def on_button_clicked(self, button_name):
        QMessageBox.information(self, "Button Clicked", f"You clicked: {button_name}")
            
    def item_clicked(self, event):
        item = self.graphics_scene.items(event.scenePos())[0]
        item.setBrush(QBrush(QColor("yellow")))
        print(f"Item clicked: {type(item).__name__} {item.x()}, {item.y()}")

    def clear_notes(self):
        self.graphics_scene.items().clear()

    def show_notes(self, notes):
        for pos in notes:
            self.draw_note(pos)
            
    def draw_note(self, t):
        noteCtrl = NoteControl(QRectF(t[0], t[1], 10, 10))
        noteCtrl.mousePressEvent = self.item_clicked
        self.graphics_scene.addItem(noteCtrl)   

num_tuples = 1000
tuples_list = TestHelper.gimme_sample_notes(num_tuples, 500, 500)
    
app = QApplication(sys.argv)
notepadApp = MainWindow()
notepadApp.showMaximized()
notepadApp.show_notes(tuples_list)
sys.exit(app.exec_())
