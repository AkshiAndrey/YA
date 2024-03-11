import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSizePolicy
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit, QPushButton


class MacOrder(QWidget):
    def __init__(self):
        super(MacOrder, self).__init__()
        self.menu_checkboxes = []
        self.initUI()

    def initUI(self):
        self.pos1 = QCheckBox('Чизбургер', self)
        self.pos1.move(30, 30)

        self.pos2 = QCheckBox('Гамбургер', self)
        self.pos2.move(30, 60)

        self.pos3 = QCheckBox('Кока-Кола', self)
        self.pos3.move(30, 90)

        self.pos4 = QCheckBox('Нагетсы', self)
        self.pos4.move(30, 120)

        self.menu_checkboxes = [self.pos1, self.pos2, self.pos3, self.pos4]

        self.result = QPlainTextEdit(self)
        self.result.setEnabled(False)
        self.result.move(30, 180)
        self.result.resize(300, 200)

        self.order_btn = QPushButton('Заказать', self)
        self.order_btn.resize(70, 30)
        self.order_btn.move(30, 150)
        self.order_btn.clicked.connect(self.order)

        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Заказ в Макдональдсе')

    def order(self):
        self.result.clear()
        self.result.appendPlainText('Ваш заказ:')
        self.result.appendPlainText('')
        for i in self.menu_checkboxes:
            if i.isChecked():
                self.result.appendPlainText(i.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MacOrder()
    ex.show()
    sys.exit(app.exec())