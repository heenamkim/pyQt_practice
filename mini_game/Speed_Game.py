import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        import random

        self.k = 1
        self.num1 = 0
        self.num2 = 0

        self.Menu = QLabel('  누가 누가 더 가깝게 누르나', self)
        self.Menu.setGeometry(QtCore.QRect(50, 50, 50, 50))
        self.Menu.setFont(QtGui.QFont("궁서", 15))
        self.Menu.move(0, 20)
        self.Menu.resize(400, 100)

        random_number = random.randrange(1, 100)
        self.number = QLabel(str(random_number), self)
        self.number.setGeometry(QtCore.QRect(50, 50, 50, 50))
        self.number.setFont(QtGui.QFont("궁서", 15))
        self.number.setStyleSheet("Color: red")
        self.number.move(180, 100)
        self.number.resize(50, 30)

        self.name_number = []
        name = ['Player1', 'Player2']
        for i in range(2):
            self.name_number.append(QLabel(name[i], self))
            self.name_number[i].move(15 + (225 * i), 130)
            self.name_number[i].resize(170, 50)
            self.name_number[i].setFont(QtGui.QFont("궁서", 15))

        self.name_number = []
        name = ['0', '0']
        for i in range(2):
            self.name_number.append(QLabel(name[i], self))
            self.name_number[i].move(80 + (215 * i), 185)
            self.name_number[i].resize(50, 30)
            self.name_number[i].setFont(QtGui.QFont("궁서", 15))

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(40, 280, 350, 40)

        self.btn = QPushButton('Start', self)
        self.btn.move(150, 340)
        self.btn.resize(100, 50)
        self.btn.setStyleSheet('color: red')
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.result = QLabel('00000', self)
        self.result.setGeometry(QtCore.QRect(50, 50, 50, 50))
        self.result.setFont(QtGui.QFont("궁서", 20))
        self.result.move(50, 410)
        self.result.resize(300, 40)
        self.result.setStyleSheet('background: red')

        self.setWindowTitle('누가누가 더 가깝게 누르나 게임')
        self.move(300, 300)
        self.resize(400, 500)
        self.setStyleSheet('background: white')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            if self.k % 2 == 0:
                self.name_number[0].setText(str(self.step))
            else:
                self.name_number[1].setText(str(self.step))
            self.step = 0

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
            if self.k % 2 == 0:
                self.name_number[0].setText(str(self.step))
            else:
                self.name_number[1].setText(str(self.step))
                self.btn.clicked.connect(self.endResult)

            self.step = 0
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            self.k += 1


    def endResult(self, state, btn):
        self.num1 = self.name_number[0].text()
        self.num2 = self.name_number[1].text()

        if random_number < int(self.num1):
            self.num1 = int(self.num1) - random_number
        else:
            self.num1 = random_number - int(self.num1)

        if random_number < int(self.name2):
            self.num2 = int(self.name2) - random_number
        else:
            self.num2 = random_number - int(self.name2)

        if self.num1 < self.num2:
            self.result.setText('Player1')
        else:
            self.result.setText('Player2')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())