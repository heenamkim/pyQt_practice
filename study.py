import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


	def initUI(self):

		self.dashboard = QLineEdit('0', self)
		self.dashboard.move(20, 20)
		self.dashboard.resize(335, 60)
		self.dashboard.setAlignment(QtCore.Qt.AlignRight)
		f = self.dashboard.font()
		f.setPointSize(30)
		self.dashboard.setFont(f)

		self.btnOp = []
		opStr = ['AC', 'C', '%', '.', '/', 'x', '-', '+', '=']
		for c in range(3):
			self.btnOp.append(QPushButton(opStr[c], self))
			self.btnOp[c].move(20+c*85, 100)
			self.btnOp[c].resize(80, 50)

		self.btnOp.append(QPushButton(opStr[3], self))
		self.btnOp[3].move(190, 320)
		self.btnOp[3].resize(80, 50)

		for r in range(4, 9):
			self.btnOp.append(QPushButton(opStr[r], self))
			self.btnOp[r].move(275, 100+(r-4)*55)
			self.btnOp[r].resize(80, 50)
			self.btnOp[r].setStyleSheet('background:orange')
			self.btnOp[r].clicked.connect(\
							lambda state, btn = self.btnOp[r] :self.pushOperator(state, btn))

		self.numKey = []
		self.numKey.append(QPushButton('0', self))
		self.numKey[0].move(20, 320)
		self.numKey[0].resize(165, 50)
		for r in range(3):
			for c in range(1, 4):
					self.numKey.append(QPushButton('%d' %(c+r*3), self))
					self.numKey[c+r*3].move(20+(c-1)*85, 265-(r*55))
					self.numKey[c+r*3].resize(80, 50)
					self.numKey[c+r*3].clicked.connect(\
								lambda state, btn = self.numKey[c+r*3] :self.writeNumber(state, btn))
		self.setWindowTitle('Jiniz Calculator')
		self.setGeometry(300, 300, 375, 390)
		self.show()

	def writeNumber(self, state, btn):
		num = self.dashboard.text()
		if int(num) == 0:
			num = btn.text()
		else:
			num += btn.text()
		self.dashboard.setText(num)

	def pushOperator(self, state, btn):
		if self.op == '':
			self.n1 = self.dashboard.text()
		else:
			self.preOpBtn.setStyleSheet('background:orange')

		self.op = btn.text()
		self.preOpBtn = btn
		btn.setStyleSheet('background:white')

	def calc(a, b, op):

		if op == '+':
			return a+b
		elif op == '-':
			return a-b
		elif op == '*':
			return a*b
		elif op == '/':
			return



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())