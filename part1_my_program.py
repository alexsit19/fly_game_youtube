#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys

class Main_Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 500, 300)
        self.menu = self.menuBar()
        self.file = self.menu.addMenu('&File')
        self.settings = self.menu.addMenu('&settings')
        self.exit = QAction('exit', self)
        self.settings_win = QAction('settings', self)
        self.file.addAction(self.exit)
        self.settings.addAction(self.settings_win)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Main_Window()
    myapp.show()
    sys.exit(app.exec_())