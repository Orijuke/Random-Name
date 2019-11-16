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

    def clicked_b(self):
        self.need_draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        if not self.need_draw:
            return
        qp.begin(self)
        qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
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