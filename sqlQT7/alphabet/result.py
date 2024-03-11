import sys
import sqlite3
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QStatusBar, QWidget, QHBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Фильмы по алфавиту")
        self.resize(800, 600)

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Год", "Жанр", "Продолжительность"])

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        alphabet = [chr(ord('А') + i) for i in range(32)]

        self.buttons = []
        for letter in alphabet:
            button = QPushButton(letter)
            button.setObjectName(letter)
            button.setMinimumWidth(10)
            button.clicked.connect(lambda state, x=letter: self.filter_movies(x))
            self.buttons.append(button)
            layout1.addWidget(button)

        layout.addItem(layout1)
        layout.addWidget(self.tableWidget)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.load_movies()

    def load_movies(self):
        conn = sqlite3.connect('films_db.sqlite')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM films")
        movies = cursor.fetchall()

        self.tableWidget.setRowCount(len(movies))
        for row, movie in enumerate(movies):
            for col, item in enumerate(movie):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))

        conn.close()

    def filter_movies(self, letter):
        conn = sqlite3.connect('films_db.sqlite')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM films WHERE title LIKE '{letter}%'")
        filtered_movies = cursor.fetchall()

        self.tableWidget.setRowCount(len(filtered_movies))
        for row, movie in enumerate(filtered_movies):
            for col, item in enumerate(movie):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))

        self.statusBar.showMessage(
            f"Нашлось {len(filtered_movies)} записей" if len(filtered_movies) > 0 else "К сожалению, ничего не нашлось")

        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
