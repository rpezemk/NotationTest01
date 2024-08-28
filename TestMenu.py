import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window properties
        self.setWindowTitle("PyQt Menu with Submenus Example")
        self.setGeometry(100, 100, 600, 400)

        # Initialize the menu bar
        self.init_menu()

    def init_menu(self):
        # Create the main menu bar
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")

        # New action
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        # Open action
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Submenu under File
        sub_menu = QMenu("Import", self)
        import_csv_action = QAction("Import CSV", self)
        import_json_action = QAction("Import JSON", self)

        # Add actions to the submenu
        sub_menu.addAction(import_csv_action)
        sub_menu.addAction(import_json_action)

        # Add the submenu to the File menu
        file_menu.addMenu(sub_menu)

        # Exit action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Help menu
        help_menu = menu_bar.addMenu("Help")

        # About action
        about_action = QAction("About", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def new_file(self):
        print("New File action triggered")

    def open_file(self):
        print("Open File action triggered")

    def about(self):
        print("About action triggered")

# Create the application object
app = QApplication(sys.argv)

# Create the main window
window = MainWindow()
window.show()

# Run the application's event loop
sys.exit(app.exec_())
