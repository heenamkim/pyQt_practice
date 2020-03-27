import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.dashboard = QLineEdit('0', self)
        self.dashboard.move(10, 20)
        self.dashboard.resize(400, 40)
        self.dashboard.setAlignment(QtCore.Qt.AlignRight)
        f = self.dashboard.font()
        f.setPointSize(20)
        self.dashboard.setFont(f)

        self.num = []
        self.num.append(QPushButton('0', self))
        self.num[0].move(110, 270)
        self.num[0].resize(100, 50)
        self.num[0].setStyleSheet('background:white')
        self.num[0].clicked.connect( \
            lambda state, btn=self.num[0]: self.writeNumber(state, btn))
        for i in range(3):
            for j in range(1, 4):
                self.num.append(QPushButton('%d' % (j + (i * 3)), self))
                self.num[j + (i * 3)].move(((j - 1) * 100) + 10, (i * 50) + 120)
                self.num[j + (i * 3)].resize(100, 50)
                self.num[j + (i * 3)].setStyleSheet('background:white')
                self.num[j + (i * 3)].clicked.connect( \
                    lambda state, btn=self.num[j + (i * 3)]: self.writeNumber(state, btn))

        self.op=[]
        opk=['/','*','-','+','=']
        for k in range(5):
            self.op[k].append(QPushButton(opk[k], self))
            self.op[k].move(310, (k*50)+70)
            self.op[k].resize(100, 50)
            self.op[k].setStyleSheet('background:ivory')

        self.dec = QPushButton('.', self)
        self.dec.move(210, 270)
        self.dec.resize(100, 50)
        self.dec.setStyleSheet('background:ivory')

        op1=['recet','←','%']
        for o in range(3):
            self.op1 = QPushButton(op1[o], self)
            self.op1.move((o*100)+10, 70)
            self.op1.resize(100, 50)
            if o > 0:
                self.op1.setStyleSheet('background:ivory')
            else:
                self.op1.setStyleSheet('background:red')

            self.setWindowTitle('QPushButton')
            self.setGeometry(500, 500, 430, 350)
            self.show()

    def writeNumber(self, state, btn):
        num = self.dashboard.text()
        if int(num) == 0:
            num = btn.text()
        else:
            num += btn.text()
        self.dashboard.setText(num)

    def reset(self,state, btn):
        self.dashboard.clear()
        self.dashboard.setText('0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())