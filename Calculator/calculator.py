import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.dashboard = QLineEdit("",self)
        self.dashboard.move(20, 20)
        self.dashboard.resize(335, 60)
        self.dashboard.setAlignment(QtCore.Qt.AlignRight)
        f = self.dashboard.font()
        f.setPointSize(30)
        self.dashboard.setFont(f)

        self.dashboard2 = QLineEdit("", self)
        self.dashboard2.move(20, 85)
        self.dashboard2.resize(335, 60)
        self.dashboard2.setAlignment(QtCore.Qt.AlignRight)
        f = self.dashboard2.font()
        f.setPointSize(30)
        self.dashboard2.setFont(f)

        self.btnOp = []
        opStr = ['AC', 'C', '%', '.', '/', '*', '-', '+', '=']
        for c in range(3):
            self.btnOp.append(QPushButton(opStr[c], self))
            self.btnOp[c].move(20 + c * 85, 150)
            self.btnOp[c].resize(80, 50)
            self.btnOp[c].setStyleSheet('background:white')

        self.btnOp.append(QPushButton(opStr[3], self))
        self.btnOp[3].move(190, 370)
        self.btnOp[3].resize(80, 50)
        self.btnOp[3].setStyleSheet('background:white')
        self.btnOp[3].clicked.connect( \
            lambda state, btn=self.btnOp[3]: self.dot(state, btn))

        for r in range(4, 9):
            self.btnOp.append(QPushButton(opStr[r], self))
            self.btnOp[r].move(275, 150 + (r - 4) * 55)
            self.btnOp[r].resize(80, 50)
            self.btnOp[r].setStyleSheet('background:white')
            self.btnOp[r].clicked.connect( \
                lambda state, btn=self.btnOp[r]: self.MakeResult(state, btn))


        for i in range(4, 8):
            self.btnOp[i].clicked.connect( \
                lambda state, btn=self.btnOp[i]: self.writeNumber(state, btn))

        self.btnOp[0].setStyleSheet('background:red')
        self.btnOp[0].clicked.connect( \
            lambda state, btn=self.btnOp[0]: self.reset(state, btn))

        self.btnOp[1].clicked.connect( \
            lambda state, btn=self.btnOp[1]: self.clear(state, btn))

        self.btnOp[2].clicked.connect( \
            lambda state, btn=self.btnOp[2]: self.per(state, btn))




        self.numKey = []
        self.numKey.append(QPushButton('0', self))
        self.numKey[0].move(20, 370)
        self.numKey[0].resize(165, 50)
        self.numKey[0].setStyleSheet('background:white')
        self.numKey[0].clicked.connect( \
            lambda state, btn=self.numKey[0]: self.writeNumber(state, btn))
        for r in range(3):
            for c in range(1, 4):
                self.numKey.append(QPushButton('%d' % (c + r * 3), self))
                self.numKey[c + r * 3].move(20 + (c - 1) * 85, 315 - (r * 55))
                self.numKey[c + r * 3].resize(80, 50)
                self.numKey[c + r * 3].setStyleSheet('background:white')
                self.numKey[c + r * 3].clicked.connect( \
                    lambda state, btn=self.numKey[c + r * 3]: self.writeNumber(state, btn))

        self.setWindowTitle('Jiniz Calculator')
        self.setGeometry(300, 300, 375, 430)
        self.show()

    def writeNumber(self, state, btn):
        num = self.dashboard.text()
        now_num = btn.text()
        self.dashboard.setText(num+now_num)

    def MakeResult(self, state, btn):
        result = eval(self.dashboard.text())
        self.dashboard2.setText(str(result))
        self.dashboard.setText(str(result))
        if btn == self.btnOp[8]:
            result = 0
            self.dashboard2.setText(str(result))


    def dot(self, state, btn):
        num = self.dashboard.text()
        if num == "":
            self.dashboard.setText('0.')
        else:
            self.dashboard.setText(str(num)+'.')


    def per(self, state, btn):
        num = self.dashboard.text()
        if btn != "":
            num = int(num) *0.01
        else:
            num = btn.text()
        self.dashboard.setText(str(num))

    def reset(self, state, btn):
        self.dashboard.clear()
        self.dashboard2.setText('0')

    def clear(self, state, btn):
        num = self.dashboard.text()
        num = num[:-1]
        self.dashboard.setText(num)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())