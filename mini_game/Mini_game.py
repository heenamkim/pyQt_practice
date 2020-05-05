import sys
from PyQt5.QtWidgets import *
from PyQt5 import *



class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.Menu = QLabel('      M e n u',self)
        self.Menu.setGeometry(QtCore.QRect(50,50,50,50))
        self.Menu.setFont(QtGui.QFont("궁서",25))
        self.Menu.move(0, 20)
        self.Menu.resize(400, 100)
        self.Menu.setStyleSheet('background: orange')

        self.menu_number = []
        number = ["1. 틱택톡게임", "2. 같은 그림 찾기", "3. 누가누가 가까이 멈추나", "4. 종료"]

        for i in range(4):
            self.menu_number.append(QPushButton(number[i], self))
            self.menu_number[i].move(50, 80*(i+2))
            self.menu_number[i].resize(300, 50)
            self.menu_number[i].clicked.connect( \
                lambda state, btn=self.menu_number[i]: self.New_File(state, btn))


        self.menu_number[3].setStyleSheet("Color: red")


        self.setWindowTitle('Mini_game')
        self.move(300, 300)
        self.resize(400, 500)
        self.show()
        self.setStyleSheet('background: white')

    def New_File(self, state, btn):

        class MyApp(QWidget):

            def __init__(self):
                super().__init__()

                self.initUI()

            def initUI(self):

                self.setWindowTitle('틱택톡게임')
                self.move(300, 300)
                self.resize(400, 500)
                self.show()
                self.setStyleSheet('background: white')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
