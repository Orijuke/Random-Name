import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.need_draw = False
        self.btn.clicked.connect(self.clicked_b)

    def clicked_b(self):
        self.need_draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        if not self.need_draw:
            return
        qp.begin(self)
        qp.setPen(QColor(255, 255, 0))
        r = randint(1, 100)
        x = randint(1, 300)
        y = randint(1, 300)
        qp.drawEllipse(x, y, r, r)
        qp.end()
        self.need_draw = False


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())