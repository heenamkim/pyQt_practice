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

        self.result = QLabel('0',self)
        self.result.setGeometry(QtCore.QRect(50, 50, 50, 50))
        self.result.setFont(QtGui.QFont("궁서", 30))
        self.result.move(30, 110)
        self.result.resize(100, 30)
        # self.result.setStyleSheet('background: red')

        self.setWindowTitle('누가누가 더 가깝게 누르나 게임')
        self.move(300, 300)
        self.resize(400, 500)
        self.setStyleSheet('background: white')
        self.show()

    def timerEvent(self, e):
        if self. k % 2 == 1:
            if self.step >= 100:
                self.timer.stop()
                self.btn.setText('Finished')
                self.name_number[0].setText(str(self.step))
                self.step = 0

        elif self. k % 2 == 0:
            if self.step >= 100:
                self.timer.stop()
                self.btn.setText('Finished')
                self.name_number[1].setText(str(self.step))
                self.step = 0

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.k % 2 == 0:
            if self.timer.isActive():
                self.timer.stop()
                self.btn.setText('Start')
                self.name_number[0].setText(str(self.step))
                self.step = 0
            else:
                self.timer.start(100, self)
                self.btn.setText('Stop')
                self.k += 1
                self.endResult()
                # self.btn.clicked.connect(self.endResult)

        else:
            if self.timer.isActive():
                self.timer.stop()
                self.btn.setText('Start')
                self.name_number[1].setText(str(self.step))
                self.step = 0
            else:
                self.timer.start(100, self)
                self.btn.setText('Stop')
                self.k += 1

    def endResult(self):
        num1 = self.name_number[0].text()
        num2 = self.name_number[1].text()

        if random_number < int(num1):
            num1 = int(num1) - random_number
        else:
            num1 = random_number - int(num1)

        if random_number < int(name2):
            num2 = int(name2) - random_number
        else:
            num2 = random_number - int(name2)

        if num1 < num2:
            self.result.setText(str(num1))
        else:
            self.result.setText(str(num2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())