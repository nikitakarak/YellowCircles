from random import randint
from PyQt5 import uic, Qt, QtCore, QtGui
from PyQt5.Qt import Qt, QPointF
from PyQt5.QtGui import QPen, QBrush, QColor, QPainter
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QGraphicsScene)
from UI import Ui_MainWindow


class RandomColorCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.circle_pen = QPen()

        scene = QGraphicsScene()
        scene.setBackgroundBrush(QBrush(Qt.darkGray))
        self.screen_gv.setRenderHint(QPainter.Antialiasing + QPainter.SmoothPixmapTransform)
        self.screen_gv.setScene(scene)

        self.create_circle_btn.clicked.connect(self.create_circle_handler)

    def create_circle_handler(self):
        d = randint(50, min(self.screen_gv.width(), self.screen_gv.height()))
        self.circle_pen.setColor(QColor(randint(50, 255), randint(50, 255), randint(50, 255), 255))
        item = self.screen_gv.scene().addEllipse(0, 0, d, d, self.circle_pen)
        item.setPos(QPointF(-d / 2, -d / 2))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = RandomColorCircles()
    ex.show()
    sys.exit(app.exec_())
