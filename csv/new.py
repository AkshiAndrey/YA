import csv
import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.loadTable('commands.txt')
        self.color_row(0, QColor(0, 150, 100))
        self.setWindowTitle('Робо Биатлон')
        self.pushButton.clicked.connect(self.save_2_csv)

    def loadTable(self, table_name):
        with open(table_name, 'r', encoding="utf8") as file:
            reader = file.readlines()
            title = reader[0].split()
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader[1:]):
                if i == 10:
                    break
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row.split()):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

    def save_2_csv(self):
        with open('results.csv', 'w', newline='', encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)
            # Получение списка заголовков
            writer.writerow(
                [self.tableWidget.horizontalHeaderItem(i).text()
                 for i in range(self.tableWidget.columnCount())])
            for i in range(self.tableWidget.rowCount()):
                row = []
                for j in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(i, j)
                    if item is not None:
                        row.append(item.text())
                writer.writerow(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
