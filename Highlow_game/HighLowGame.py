import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import random


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dashboard2.setText("Game Start")

        self.n = random.randint(1, 100)

    def initUI(self):

        self.dashboard = QLineEdit(" ", self)
        self.dashboard.move(10, 20)
        self.dashboard.resize(300, 40)
        self.dashboard.setAlignment(QtCore.Qt.AlignRight)
        f = self.dashboard.font()
        f.setPointSize(20)
        self.dashboard.setFont(f)

        self.dashboard2 = QLineEdit(self)
        self.dashboard2.move(10, 65)
        self.dashboard2.resize(300, 40)
        self.dashboard2.setAlignment(QtCore.Qt.AlignRight)
        f = self.dashboard2.font()
        f.setPointSize(20)
        self.dashboard2.setFont(f)

        self.num = []
        self.num.append(QPushButton('0', self))
        self.num[0].move(110, 270)
        self.num[0].resize(100, 50)
        self.num[0].setStyleSheet('background:white')
        self.num[0].clicked.connect( \
            lambda state, btn=self.num[0]: self.writeNumber(state, btn))
        for i in range(3):
            for j in range(1, 4):
                self.num.append(QPushButton('%d' % (j+(i*3)), self))
                self.num[j+(i*3)].move(((j-1) * 100) + 10, (i * 50) + 120)
                self.num[j+(i*3)].resize(100, 50)
                self.num[j+(i*3)].setStyleSheet('background:white')
                self.num[j+(i*3)].clicked.connect( \
                    lambda state, btn = self.num[j+(i*3)] :self.writeNumber(state, btn))

        self.ok = QPushButton('확인', self)
        self.ok.move(210, 270)
        self.ok.resize(100, 50)
        self.ok.setStyleSheet('background:orange')
        self.ok.clicked.connect( \
            lambda state, btn=self.ok: self.result(state, btn))

        self.cancel = QPushButton('취소',self)
        self.cancel.move(10, 270)
        self.cancel.resize(100, 50)
        self.cancel.setStyleSheet('background:red')
        self.cancel.clicked.connect(\
            lambda state, btn=self.cancel: self.reset(state, btn))

        self.setWindowTitle('High Low Game')
        self.move(300, 300)
        self.resize(350, 350)
        self.show()

    def writeNumber(self, state, btn):
        num = self.dashboard.text()
        if num == " ":
            num = btn.text()
        else:
            num += btn.text()
        self.dashboard.setText(num)
        self.dashboard2.setText(" ")

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def reset(self,state, btn):
        num = self.dashboard.text()
        if num != " ":
            num = int(num) // 10

        self.dashboard.setText(str(num))

    def result(self,state,btn):
        num = self.dashboard.text()
        if int(num) < self.n:
            self.dashboard2.setText('High')
        elif int(num) == self.n:
            self.dashboard2.setText("That's Right!")
        else:
            self.dashboard2.setText('Low..')
        self.dashboard.setText("")

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())