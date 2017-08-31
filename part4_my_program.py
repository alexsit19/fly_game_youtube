#-*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,\
                            QWidget, qApp, QPushButton, QHBoxLayout,\
                            QVBoxLayout, QGridLayout, QLabel

import sys
from PyQt5.QtCore import Qt, QPoint

class Window_Ui(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.button = QPushButton("1", self)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        self.button4 = QPushButton("4", self)
        self.button5 = QPushButton("5", self)
        self.button6 = QPushButton("6", self)
        self.grid = QGridLayout()
        self.vbox = QVBoxLayout()
        self.grid.addWidget(self.button, 0, 0)
        self.grid.addWidget(self.button2, 0, 1)
        self.grid.addWidget(self.button3, 0, 2)
        self.grid.addWidget(self.button4, 1, 0)
        self.grid.addWidget(self.button5, 1, 1)
        self.grid.addWidget(self.button6, 1, 2)

        #self.vbox.addLayout(self.grid)
        self.setLayout(self.grid)



class Main_Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Window_Ui()
        self.setCentralWidget(self.ui)
        self.setGeometry(300, 300, 500, 300)
        self.menu = self.menuBar()
        self.file = self.menu.addMenu('&&File')
        self.settings = self.menu.addMenu('&settings')
        self.exit = QAction('exit', self)
        self.button = QPushButton("Старт")
        self.button.move(10, 10)
        self.settings_win = QAction('settings', self)
        self.file.addAction(self.exit)
        self.settings.addAction(self.settings_win)
        self.exit.triggered.connect(qApp.quit)
        self.settings_win.triggered.connect(self.settings_show)

    def settings_show(self):
        w = QWidget(self, Qt.Window)
        w.setWindowModality(Qt.WindowModal)
        w.resize(300, 200)
        w.move(self.geometry().center() - w.rect().center() - QPoint(0, 30))
        w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Main_Window()
    myapp.show()
    sys.exit(app.exec_())
