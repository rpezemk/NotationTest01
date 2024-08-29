import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QSplitter, QVBoxLayout, QToolBar, QAction, QSplitterHandle
from PyQt5.QtCore import Qt

class CustomSplitterHandle(QSplitterHandle):
    def __init__(self, orientation, parent):
        super().__init__(orientation, parent)
        self.setStyleSheet("background-color: red;")  # Red splitter handle

class CustomSplitter(QSplitter):
    def createHandle(self):
        return CustomSplitterHandle(self.orientation(), self)

class CustomPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create the first section
        self.section1 = QLabel("Section 1", self)
        self.section1.setAlignment(Qt.AlignCenter)

        # Create the second section
        self.section2 = QLabel("Section 2", self)
        self.section2.setAlignment(Qt.AlignCenter)

        # Create the third section
        self.section3 = QLabel("Section 3", self)
        self.section3.setAlignment(Qt.AlignCenter)

        # Create a custom splitter
        self.splitter = CustomSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.section1)
        self.splitter.addWidget(self.section2)
        self.splitter.addWidget(self.section3)

        # Set initial sizes
        self.splitter.setSizes([200, 200, 200])

        # Set the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.splitter)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window with Custom Splitter Handle and Toolbar")
        self.setGeometry(100, 100, 600, 400)

        # Create an instance of CustomPanel
        self.custom_panel = CustomPanel()
        self.setCentralWidget(self.custom_panel)

        # Create a toolbar at the bottom
        self.toolbar = QToolBar("Bottom Toolbar")
        self.addToolBar(Qt.BottomToolBarArea, self.toolbar)

        # Create actions for hiding and showing the second section
        self.hide_action = QAction("Hide Section 2", self)
        self.show_action = QAction("Show Section 2", self)

        # Add actions to the toolbar
        self.toolbar.addAction(self.hide_action)
        self.toolbar.addAction(self.show_action)

        # Connect the actions to the corresponding methods
        self.hide_action.triggered.connect(self.hide_section_2)
        self.show_action.triggered.connect(self.show_section_2)

    def hide_section_2(self):
        # Hide the second section
        self.custom_panel.section2.hide()
        self.custom_panel.splitter.setSizes([300, 0, 300])  # Adjust sizes after hiding

    def show_section_2(self):
        # Show the second section
        self.custom_panel.section2.show()
        self.custom_panel.splitter.setSizes([200, 200, 200])  # Adjust sizes after showing

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec_())
