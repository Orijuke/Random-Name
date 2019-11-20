import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.need_draw = False
        self.btn.clicked.connect(self.clicked_b)
        self.circle = [0, 0, 0, QColor(0, 0, 0)]

    def clicked_b(self):
        self.need_draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.need_draw:
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            self.circle[3] = color
            r = randint(1, 100)
            self.circle[0] = r
            x = randint(1, 300)
            y = randint(1, 300)
            self.circle[1], self.circle[2] = x, y
        qp.setPen(self.circle[3])
        qp.drawEllipse(self.circle[1], self.circle[2], self.circle[0], self.circle[0])
        qp.end()
        self.need_draw = False


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())