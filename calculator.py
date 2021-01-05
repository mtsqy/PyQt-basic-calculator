from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    x,y = None, None
    userisTyping = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.connectBtn()
        #connect button
    def connectBtn(self):
        self.numBtn_0.clicked.connect(self.numPressed)
        self.numBtn_1.clicked.connect(self.numPressed)
        self.numBtn_2.clicked.connect(self.numPressed)
        self.numBtn_3.clicked.connect(self.numPressed)
        self.numBtn_4.clicked.connect(self.numPressed)
        self.numBtn_5.clicked.connect(self.numPressed)
        self.numBtn_6.clicked.connect(self.numPressed)
        self.numBtn_7.clicked.connect(self.numPressed)
        self.numBtn_8.clicked.connect(self.numPressed)
        self.numBtn_9.clicked.connect(self.numPressed)
        self.decimalBtn.clicked.connect(self.decimalPressed)
        self.plusminBtn.clicked.connect(self.unaryOperationPressed)
        self.percentBtn.clicked.connect(self.unaryOperationPressed)
        self.addBtn.clicked.connect(self.binaryOperationPressed)
        self.subtractBtn.clicked.connect(self.binaryOperationPressed)
        self.multiplyBtn.clicked.connect(self.binaryOperationPressed)
        self.divideBtn.clicked.connect(self.binaryOperationPressed)
        self.equalsBtn.clicked.connect(self.equalsPressed)
        self.clearBtn.clicked.connect(self.clearPressed)
        self.addBtn.setCheckable(True)
        self.subtractBtn.setCheckable(True)
        self.multiplyBtn.setCheckable(True)
        self.divideBtn.setCheckable(True) 
    def numPressed(self):
        button = self.sender()
        if((self.addBtn.isChecked() or
        self.subtractBtn.isChecked() or
        self.multiplyBtn.isChecked() or
        self.divideBtn.isChecked()) and (not self.userisTyping)):
            updtDisplay = format(float(button.text()),'.15g')
            self.userisTyping = True
        else:
            if (('.' in self.displayRes.text()) and (button.text() == "0")):
                updtDisplay = format(self.displayRes.text() + button.text(),'.15')
            else:
                updtDisplay = format(float(self.displayRes.text() + button.text()),'.15g')
        self.displayRes.setText(updtDisplay)
    def decimalPressed(self):
        if "." not in self.displayRes.text():
            self.displayRes.setText(self.displayRes.text() + '.')
    def unaryOperationPressed(self):
        button = self.sender()
        displayNumber = float(self.displayRes.text())
        if button.text() == '+/-':
            displayNumber = displayNumber * -1
        else:
            displayNumber = displayNumber * 0.01
        updtDisplay = format(displayNumber,'.15g')
        self.displayRes.setText(updtDisplay)
    def binaryOperationPressed(self):
        button = self.sender()
        self.x = float(self.displayRes.text())
        button.setChecked(True)
    def equalsPressed(self):
        self.y = float(self.displayRes.text())
        if self.addBtn.isChecked():
            displayNumber = self.x + self.y
            updtDisplay = format(displayNumber,'.15g')
            self.displayRes.setText(updtDisplay)
            self.addBtn.setChecked(False)
        elif self.subtractBtn.isChecked():
            displayNumber = self.x - self.y
            updtDisplay = format(displayNumber,'.15g')
            self.displayRes.setText(updtDisplay)
            self.subtractBtn.setChecked(False)
        elif self.multiplyBtn.isChecked():
            displayNumber = self.x * self.y
            updtDisplay = format(displayNumber,'.15g')
            self.displayRes.setText(updtDisplay)
            self.multiplyBtn.setChecked(False)
        elif self.divideBtn.isChecked():
            displayNumber = self.x / self.y
            updtDisplay = format(displayNumber,'.15g')
            self.displayRes.setText(updtDisplay)
            self.divideBtn.setChecked(False)
        self.userisTyping = False
    def clearPressed(self):
        self.addBtn.setChecked(False)
        self.subtractBtn.setChecked(False)
        self.multiplyBtn.setChecked(False)
        self.divideBtn.setChecked(False)
        self.userisTyping = False
        self.displayRes.setText("0")

