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
        self.btn_start = QPushButton("старт", self)
        self.btn_up = QPushButton("вверх", self)
        self.btn_down = QPushButton("вниз", self)
        self.btn_left = QPushButton("влево", self)
        self.btn_right = QPushButton("вправо", self)
        self.btn_forw = QPushButton("вперёд", self)
        self.btn_back = QPushButton("назад", self)

        self.move_text = QLabel()
        self.move_text.setText("<center><b><font size=10>Ход</font></b></center>")
        self.time_ramain = QLabel()
        self.time_ramain.setText("<center><b><font size=10>Осталось: 5</font></b></center>")
        self.text_coord = QLabel()
        self.text_coord.setText("<center><b><font size=10>1:1:1</font></b></center>")

        self.grid = QGridLayout()
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.vbox.addWidget(self.btn_start)
        self.hbox.addWidget(self.time_ramain)
        self.hbox.addWidget(self.move_text)
        self.hbox.addWidget(self.text_coord)

        self.grid.addWidget(self.btn_right, 0, 0)
        self.grid.addWidget(self.btn_forw, 0, 1)
        self.grid.addWidget(self.btn_up, 0, 2)
        self.grid.addWidget(self.btn_left, 1, 0)
        self.grid.addWidget(self.btn_back, 1, 1)
        self.grid.addWidget(self.btn_down, 1, 2)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.grid)
        self.setLayout(self.vbox)



class Main_Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Window_Ui()
        self.setCentralWidget(self.ui)
        self.setGeometry(300, 300, 700, 400)
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