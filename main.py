import sys

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QGridLayout, QLabel


data_digits = '0123456789'
data_dot = '.'
data_operators = '/*-+%^'
data_clear = 'C'
data_equal = '='

class Calculator:
    def get_calculate(self, a, b, operand):
        res = 0
        if operand == '+':
           res = self.__plus(a, b)
        elif operand == '-':
            res = self.__minus(a, b)
        elif operand == '*':
            res = self.__mult(a, b)
        elif operand == '^':
            res = self.__degree(a, b)
        elif operand == '/':
            res = self.__divide(a, b)
        elif operand == '%':
            res = self.__mod(a, b)
        return res

    def __plus(self, a, b):
        return a + b

    def __minus(self, a, b):
        return a - b

    def __mult(self, a, b):
        return a * b

    def __divide(self, a, b):
        return round(a / b, 4)

    def __degree(self, a, b):
        return a ** b

    def __mod(self, a, b):
        return a % b


class MainWindow(QMainWindow, Calculator):
    status_line = ''
    step = 0
    a = ''
    b = ''
    sign = ''

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kolambulator')
        self.setMinimumSize(QSize(300, 450))
        # create container
        self.container = QWidget()
        self.setCentralWidget(self.container)
        self.container.setStyleSheet(".QWidget {background-color: black}")

        vbox_layout = QVBoxLayout()
        # create widgets
        self.curent_result = QLabel()
        self.curent_result.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.curent_result.setStyleSheet(".QLabel {color: white; font-size: 15px; font-family: 'sans-serif'}")
        vbox_layout.addWidget(self.curent_result)

        self.line_output = QLabel()
        self.line_output.setFont(QFont("sans-serif", 38, QFont.Bold))
        self.line_output.setStyleSheet('color: white;')
        self.line_output.setAlignment(Qt.AlignTop | Qt.AlignRight)
        vbox_layout.addWidget(self.line_output)

        self.buttons = {}
        for ch in data_digits + data_operators + data_clear + data_dot + data_equal:
            btn = QPushButton(f'{ch}')
            btn.clicked.connect(self.btn_clicked)
            btn.setMinimumSize(QSize(40, 50))
            btn.setFont(QFont("sans-serif", 14, QFont.Normal))
            btn.setStyleSheet('.QPushButton {color: white; background: black; border: 2px solid white;}'
                              ' .QPushButton:hover {background: #CF9FFF;}')

            self.buttons[ch] = btn
        gridbox = QGridLayout()
        vbox_layout.addLayout(gridbox)

        gridbox.addWidget(self.buttons['C'], 0, 0)
        gridbox.addWidget(self.buttons['%'], 0, 1)
        gridbox.addWidget(self.buttons['^'], 0, 2)
        gridbox.addWidget(self.buttons['/'], 0, 3)

        gridbox.addWidget(self.buttons['7'], 1, 0)
        gridbox.addWidget(self.buttons['8'], 1, 1)
        gridbox.addWidget(self.buttons['9'], 1, 2)
        gridbox.addWidget(self.buttons['*'], 1, 3)

        gridbox.addWidget(self.buttons['4'], 2, 0)
        gridbox.addWidget(self.buttons['5'], 2, 1)
        gridbox.addWidget(self.buttons['6'], 2, 2)
        gridbox.addWidget(self.buttons['+'], 2, 3)

        gridbox.addWidget(self.buttons['1'], 3, 0)
        gridbox.addWidget(self.buttons['2'], 3, 1)
        gridbox.addWidget(self.buttons['3'], 3, 2)
        gridbox.addWidget(self.buttons['-'], 3, 3)

        gridbox.addWidget(self.buttons['0'], 4, 0)
        gridbox.addWidget(self.buttons['.'], 4, 1)
        gridbox.addWidget(self.buttons['='], 4, 2, 0, 2)

        self.container.setLayout(vbox_layout)

    def btn_clicked(self):
        ch = self.sender().text()
        if self.step == 0 and ch in data_digits:
            self.a += ch
            self.status_line = self.a
        elif self.step == 0 and ch in data_dot and self.a.count('.') == 0:
            self.a += ch
            self.status_line = self.a
        elif self.step == 0 and ch in data_operators:
            self.sign = ch
            self.step += 1
            self.status_line = ch
        elif self.step == 1 and ch in data_digits:
            if self.status_line[0] in data_operators:
                self.status_line = ''
            self.b += ch
            self.status_line = self.b
        elif self.step == 1 and ch in data_dot and self.b.count('.') == 0:
            self.b += ch
            self.status_line = self.b
        elif self.step == 1 and self.b != '' and ch == data_equal:
            math_res = str(self.get_calculate(float(self.a), float(self.b), self.sign))
            self.a = math_res
            self.b = ''
            self.sign = ''
            self.step = 0
            self.status_line = math_res
        elif ch == 'C':
            self.a = ''
            self.b = ''
            self.sign = ''
            self.status_line = ''
            self.step = 0

        self.curent_result.setText(self.a + self.sign + self.b)
        self.line_output.setText(self.status_line)





app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()