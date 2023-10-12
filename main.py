import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, 300, 400)

        self.result_line = QLineEdit()
        self.result_line.setReadOnly(True)

        self.button_grid = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        vbox = QVBoxLayout()

        vbox.addWidget(self.result_line)

        for row in self.button_grid:
            hbox = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_click)
                hbox.addWidget(button)
            vbox.addLayout(hbox)

        self.setLayout(vbox)

    def on_button_click(self):
        sender = self.sender()
        if sender.text() == '=':
            try:
                result = str(eval(self.result_line.text()))
                self.result_line.setText(result)
            except Exception:
                self.result_line.setText("Ошибка")
        else:
            current_text = self.result_line.text()
            new_text = current_text + sender.text()
            self.result_line.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())
