import sys
from PyQt5.QtWidgets import *
from PyQt5 import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.count = 1

        self.Menu = QLabel('  틱 택 톡 게 임', self)
        self.Menu.setGeometry(QtCore.QRect(50, 50, 50, 50))
        self.Menu.setFont(QtGui.QFont("궁서", 25))
        self.Menu.move(0, 20)
        self.Menu.resize(400, 100)


        self.game_number = []
        self.game_number2 = []

        for a in range(3):
            for b in range(1, 4):
                self.game_number.append(QPushButton(self))
                self.game_number[(a*3)+(b-1)].move(30 + (110 * a), 50 + (90 * b))
                self.game_number[(a*3)+(b-1)].resize (100, 80)
                # self.game_number[(a*3)+(b-1)].clicked.connect(self.gameStart)
                # self.game_number[(a*3)+(b-1)].clicked.connect( \
                #     lambda state, btn=self.game_number[(a*3)+(b-1)]: self.gameStart(state, btn))

        self.menu_number = []
        name = ['다시 시작', '다시 누르기', '확인']
        for i in range(3):
            self.menu_number.append(QPushButton(name[i],self))
            self.menu_number[i].move(20+(130*i), 430)
            self.menu_number[i].resize(100, 50)
            self.menu_number[i].setStyleSheet("Color: red")


        self.setWindowTitle('틱택톡 게임')
        self.move(300, 300)
        self.resize(400, 500)
        self.setStyleSheet('background: white')
        self.show()

    # def gameStart(self):
    #     self.game_number[(a*3)+(b-1)].setText('O')
        # self.you = btn
        # self.game_number2.append(you+1)
        #  self.count += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())