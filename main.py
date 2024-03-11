import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy, QMainWindow, QAction, QLabel

EXCHANGE_RATES = {
    'Рубль': 1,
    'Доллар': 70,
    'Евро': 80,
    'Тунрик': 30
}


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()

        self.main_layout = QHBoxLayout(self)
        self.input_layout = QVBoxLayout(self)
        self.output_layout = QVBoxLayout(self)

        self.input_value = QLineEdit(self)
        self.input_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_type = QComboBox(self)
        self.input_type.addItems(EXCHANGE_RATES.keys())
        self.input_type.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.convert_button = QPushButton(self)
        self.convert_button.setText('->')
        self.convert_button.clicked.connect(self.convert)
        self.convert_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)
        self.output_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_type = QComboBox(self)
        self.output_type.addItems(EXCHANGE_RATES.keys())
        self.output_type.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_layout.addWidget(self.input_value)
        self.input_layout.addWidget(self.input_type)

        self.output_layout.addWidget(self.output_value)
        self.output_layout.addWidget(self.output_type)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.convert_button)
        self.main_layout.addLayout(self.output_layout)

        self.setLayout(self.main_layout)

    def convert(self):
        input = float(self.input_value.text()) * EXCHANGE_RATES[self.input_type.currentText()]
        output = input / EXCHANGE_RATES[self.output_type.currentText()]
        self.output_value.setText(f'{output:.2f}')

class About_window(QWidget):
    def __init__(self):
        super(About_window, self).__init__()

        self.setWindowTitle('О программе')
        self.setLayout((QVBoxLayout(self)))
        self.info = QLabel(self)
        self.info.setText('Это конвертер валют))')
        self.layout().addWidget(self.info)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Конвертер валют')
        self.setCentralWidget(ConvertWidget())

        self.about_action = QAction(self)
        self.about_action.setText('О программе')
        self.about_action.triggered.connect(self.about)
        self.menuBar().addAction(self.about_action)

        self.about_window = About_window()

    def about(self):
        self.about_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())

