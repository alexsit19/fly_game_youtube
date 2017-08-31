#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,\
                            QWidget, qApp
import sys
from PyQt5.QtCore import Qt

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
        self.exit.triggered.connect(qApp.quit)
        self.settings_win.triggered.connect(self.settings_show)

    def settings_show(self):
        w = QWidget(self, Qt.Window)
        w.setWindowModality(Qt.WindowModal)
        w.resize(300, 200)
        w.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Main_Window()
    myapp.show()
    sys.exit(app.exec_())