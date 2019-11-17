import random
from PyQt5 import uic, Qt, QtCore, QtGui
from PyQt5.Qt import Qt, QPointF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QGraphicsScene)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.yellow_pen = QPen(Qt.yellow)

        scene = QGraphicsScene()
        scene.setBackgroundBrush(QBrush(Qt.darkGray))
        self.screen_gv.setScene(scene)

        self.create_circle_btn.clicked.connect(self.create_circle_handler)

    def create_circle_handler(self):
        d = random.randint(50, min(self.screen_gv.width(), self.screen_gv.height()))
        item = self.screen_gv.scene().addEllipse(0, 0, d, d, self.yellow_pen)
        item.setPos(QPointF(-d / 2, -d / 2))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())