import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class Yellow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.run)
        self.start_draw = False
        self.point = [300, 300]

    def run(self):
        self.start_draw = True
        self.update()

    def paintEvent(self, event):
        if self.start_draw:
            self.qp = QPainter()
            self.qp.begin(self)
            side = randint(20, 100)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.drawEllipse(QPointF(self.point[0], self.point[1]), side, side)
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec())
