import sys

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QPolygonF
from PyQt5.QtWidgets import (QApplication, QPushButton, QLineEdit, QWidget)


class Square2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.color = QColor(0, 0, 0)
        self.font = QFont("sans-serif", 16)

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Квадрат-объектив")

        self.draw = QPushButton("Рисовать", self)
        self.draw.move(50, 10)

        self.k = QLineEdit(self)  # coeff
        self.k.move(50, 30)
        self.k.setText('0.8')

        self.n = QLineEdit(self)  # n
        self.n.setText('20')
        self.n.move(50, 50)

        self.do_paint = False
        self.draw.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_square(qp)
            qp.end()
            self.do_paint = False

    def draw_square(self, qp):

        p = float(self.k.text())
        # q = 1 - p
        k = 1 - p
        n = int(self.n.text())

        pen = QPen(self.color, 1)
        qp.setPen(pen)
        size = 200
        Ax, Ay = 150, 150
        Bx, By = Ax + size, Ay
        Cx, Cy = Bx, By + size
        Dx, Dy = Ax, Cy

        for i in range(n):
            polygon = QPolygonF()
            polygon << QPointF(Ax, Ay) << QPointF(Bx, By) << QPointF(Cx, Cy) << QPointF(Dx, Dy)
            qp.drawPolygon(polygon)

            Ax_new = (Bx - Ax) * k + Ax
            Ay_new = (By - Ay) * k + Ay
            Bx_new = (Cx - Bx) * k + Bx
            By_new = (Cy - By) * k + By
            Cx_new = (Dx - Cx) * k + Cx
            Cy_new = (Dy - Cy) * k + Cy
            Dx_new = (Ax - Dx) * k + Dx
            Dy_new = (Ay - Dy) * k + Dy

            Ax = Ax_new
            Ay = Ay_new
            Bx = Bx_new
            By = By_new
            Cx = Cx_new
            Cy = Cy_new
            Dx = Dx_new
            Dy = Dy_new


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square2()
    ex.show()
    sys.exit(app.exec())
