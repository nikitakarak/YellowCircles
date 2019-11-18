from random import randint
from PyQt5 import uic, Qt, QtCore, QtGui
from PyQt5.Qt import Qt, QPointF
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QGraphicsScene)
from ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.pen = QPen()

        scene = QGraphicsScene()
        scene.setBackgroundBrush(QBrush(Qt.darkGray))
        self.screen_gv.setScene(scene)

        self.create_circle_btn.clicked.connect(self.create_circle_handler)

    def create_circle_handler(self):
        d = randint(50, min(self.screen_gv.width(), self.screen_gv.height()))
        self.pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255), 255))
        item = self.screen_gv.scene().addEllipse(0, 0, d, d, self.pen)
        item.setPos(QPointF(-d / 2, -d / 2))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
