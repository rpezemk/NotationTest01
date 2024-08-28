from PyQt5.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem,
    QGraphicsRectItem, QMainWindow, QVBoxLayout, QHBoxLayout, 
    QPushButton, QWidget, QToolBar, QAction, QMenu, QMenuBar)


class ActionHelper:
    @staticmethod
    def AssignMenuEntry(qwindow: QMainWindow, action, *args) -> None:
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
            
    def AssignToolbarEntry(qwindow: QMainWindow, action, *args) -> None:
        if(len(args) == 0):
            return
        
        toolbar = getattr(qwindow, "toolBar")
        if toolbar == None:
            qwindow.toolBar = QToolBar("Toolbar", qwindow)
        
        menuName = args[0]
        intermediate = args[1:-1]
        last: str = args[-1]
        addedActionItem = QAction(last, qwindow)
        addedActionItem.triggered.connect(action)
        if len(args) == 1:
            qwindow.toolBar.addAction(addedActionItem)
            return
        else:
            lastQmenu = ActionHelper.find_submenu(qwindow.toolBar, menuName)
            if lastQmenu == None:
                lastQmenu = QMenu(menuName, qwindow)
                submenu_action = QAction(menuName, qwindow)
                submenu_action.setMenu(lastQmenu)
                qwindow.toolBar.addAction(submenu_action)
            for sub in intermediate:
                subMenu = ActionHelper.find_submenu(lastQmenu, sub)
                if subMenu == None:
                    subMenu = QMenu(sub, qwindow)
                    submenu_action = QAction(sub, qwindow)
                    submenu_action.setMenu(subMenu)
                    lastQmenu.addAction(submenu_action)
                lastQmenu = subMenu
            lastQmenu.addAction(addedActionItem)     
            
    @staticmethod
    def find_submenu(parent_menu, submenu_title):
        for action in parent_menu.actions():
            if action.menu() and action.menu().title() == submenu_title:
                return action.menu()
        return None                
    
