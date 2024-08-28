import random
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtWidgets import QGraphicsRectItem, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QWidget, QToolBar, QAction, QMenu

from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QBrush, QPen, QColor
from GUI.NoteControl import NoteControl
from Helpers.TestHelper import TestHelper
from Helpers.ActionHelper import ActionHelper

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 400, 300)
        self.view = QGraphicsView(self.scene, self)
        self.create_top_pane()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.toolBar)
        layout.addWidget(self.view)
        self.setWindowTitle("PyQt5 Canvas with Clickable Items and Top Pane")

        ActionHelper.Assign(self, self.close, "File", "Quit")
        ActionHelper.Assign(self, self.about, "Help", "About")
        ActionHelper.Assign(self, self.open_method, "File", "Open" )
        ActionHelper.Assign(self, self.save_method, "File", "Save" )
        
    def open_method(self):
        pass
    def save_method(self):
        pass
    
    def about(self):
        print("About action triggered")    
        
    def create_top_pane(self):
        # Create a toolbar as a top pane
        self.toolBar = QToolBar("Toolbar", self)
        self.addToolBar(Qt.TopToolBarArea, self.toolBar)

        # Add buttons to the toolbar
        btn1 = QAction("Button 1", self)
        btn1.triggered.connect(lambda: self.on_button_clicked("Button 1"))
        self.toolBar.addAction(btn1)

        btn2 = QAction("Button 2", self)
        btn2.triggered.connect(lambda: self.on_button_clicked("Button 2"))
        self.toolBar.addAction(btn2)

        btn3 = QAction("Button 3", self)
        btn3.triggered.connect(lambda: self.on_button_clicked("Button 3"))
        self.toolBar.addAction(btn3)
        
    def item_clicked(self, event):
        item = self.scene.items(event.scenePos())[0]
        item.setBrush(QBrush(QColor("yellow")))
        print(f"Item clicked: {type(item).__name__} {item.x()}, {item.y()}")

    def on_button_clicked(self, button_name):
        print(f"{button_name} clicked")

    def clear_notes(self):
        self.scene.items().clear()

    def show_notes(self, notes):
        for pos in notes:
            self.draw_note(pos)
            
    def draw_note(self, t):
        # Create a red circle
        noteCtrl = NoteControl(QRectF(t[0], t[1], 100, 100))
        noteCtrl.mousePressEvent = self.item_clicked
        self.scene.addItem(noteCtrl)   
        
# if __name__ == "__main__":

data = [    
    (0, 600), 
    (100, 500), 
    (200, 400), 
    (300, 300), 
    (400, 200), 
    (500, 100), 
        ]


def generate_random_tuples(num_tuples, value_range):
    tuples_list = []
    for _ in range(num_tuples):
        x_value = random.randint(0, value_range)
        y_value = random.randint(0, value_range)
        tuples_list.append((x_value, y_value))
    return tuples_list


num_tuples = 1000
tuples_list = TestHelper.gimme_sample_notes(num_tuples)
    
app = QApplication(sys.argv)
notepadApp = MainWindow()
notepadApp.showMaximized()
notepadApp.show_notes(tuples_list)
sys.exit(app.exec_())
