from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QToolBar, QAction, QMenu, QMenuBar

class ActionHelper:
    @staticmethod
    def Assign(qwindow: QMainWindow, action, *args):
        if(len(args) == 0):
            return
        menu_bar = qwindow.menuBar()
        menuName = args[0]
        intermediate = args[1:-1]
        last: str = args[-1]
        addedActionItem = QAction(last, qwindow)
        addedActionItem.triggered.connect(action)
        if len(args) == 1:
            menu_bar.addAction(addedActionItem)
        else:
            lastQmenu = ActionHelper.find_submenu(menu_bar, menuName)
            if lastQmenu == None:
                lastQmenu = QMenu(menuName, qwindow)
                menu_bar.addMenu(lastQmenu)
            for sub in intermediate:
                subMenu = ActionHelper.find_submenu(lastQmenu, sub)
                if subMenu == None:
                    subMenu = QMenu(sub, qwindow)
                    lastQmenu.addMenu(subMenu)
                    lastQmenu = subMenu
                
            lastQmenu.addAction(addedActionItem)

            
            
    @staticmethod
    def GetQMenuByName(qmenu: QMenu, entryName: str):
        children = qmenu.children()
        children2 = qmenu.findChildren(QMenu)
        asdf = ActionHelper.find_submenu(qmenu, "File")
        found = False
        res = None
        for ch in children:
            if isinstance(ch, QMenu):
                subQmenu: QMenu = ch
                if(subQmenu.title() == entryName):
                    return subQmenu
            elif isinstance(ch, QMenuBar):
                subQmenu: QMenuBar = ch
                if(subQmenu.title() == entryName):
                    return subQmenu
            elif isinstance(ch, QAction):
                qAction: QAction = ch
                pass
        
        return None
        
    def find_submenu(parent_menu, submenu_title):
        # Iterate through actions in the parent menu
        for action in parent_menu.actions():
            # Check if the action has a menu (submenu)
            if action.menu() and action.menu().title() == submenu_title:
                return action.menu()
        return None                