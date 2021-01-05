# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 456)
        font = QtGui.QFont()
        font.setPointSize(6)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #5d5d5d, stop: 1 #242528);\n"
"    border: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #5d5d5d, stop: 1 #242528);\n"
"    border: none;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.displayRes = QtWidgets.QLabel(self.centralwidget)
        self.displayRes.setGeometry(QtCore.QRect(0, 20, 271, 56))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.displayRes.setFont(font)
        self.displayRes.setStyleSheet("QLabel {\n"
"     qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"    color: #8F8C75;\n"
"    padding: 0 30px;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.displayRes.setObjectName("displayRes")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(200, 80, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.clearBtn.setFont(font)
        self.clearBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #FFCC63;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #ffffff;\n"
"}")
        self.clearBtn.setObjectName("clearBtn")
        self.factorialBtn = QtWidgets.QPushButton(self.centralwidget)
        self.factorialBtn.setGeometry(QtCore.QRect(80, 80, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.factorialBtn.setFont(font)
        self.factorialBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #6d6d6d;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.factorialBtn.setObjectName("factorialBtn")
        self.invmultiplyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.invmultiplyBtn.setGeometry(QtCore.QRect(140, 80, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.invmultiplyBtn.setFont(font)
        self.invmultiplyBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #6d6d6d;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.invmultiplyBtn.setObjectName("invmultiplyBtn")
        self.logBtn = QtWidgets.QPushButton(self.centralwidget)
        self.logBtn.setGeometry(QtCore.QRect(20, 80, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.logBtn.setFont(font)
        self.logBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #6d6d6d;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.logBtn.setObjectName("logBtn")
        self.numBtn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_7.setGeometry(QtCore.QRect(20, 200, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_7.setFont(font)
        self.numBtn_7.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_7.setObjectName("numBtn_7")
        self.numBtn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_8.setGeometry(QtCore.QRect(80, 200, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_8.setFont(font)
        self.numBtn_8.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_8.setObjectName("numBtn_8")
        self.numBtn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_9.setGeometry(QtCore.QRect(140, 200, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_9.setFont(font)
        self.numBtn_9.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_9.setObjectName("numBtn_9")
        self.multiplyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.multiplyBtn.setGeometry(QtCore.QRect(200, 200, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.multiplyBtn.setFont(font)
        self.multiplyBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #8F8C75;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.multiplyBtn.setObjectName("multiplyBtn")
        self.numBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_3.setGeometry(QtCore.QRect(140, 320, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_3.setFont(font)
        self.numBtn_3.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_3.setObjectName("numBtn_3")
        self.numBtn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_1.setGeometry(QtCore.QRect(20, 320, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_1.setFont(font)
        self.numBtn_1.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_1.setObjectName("numBtn_1")
        self.numBtn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_4.setGeometry(QtCore.QRect(20, 260, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_4.setFont(font)
        self.numBtn_4.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_4.setObjectName("numBtn_4")
        self.numBtn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_5.setGeometry(QtCore.QRect(80, 260, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_5.setFont(font)
        self.numBtn_5.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_5.setObjectName("numBtn_5")
        self.numBtn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_6.setGeometry(QtCore.QRect(140, 260, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_6.setFont(font)
        self.numBtn_6.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_6.setObjectName("numBtn_6")
        self.numBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_2.setGeometry(QtCore.QRect(80, 320, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_2.setFont(font)
        self.numBtn_2.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_2.setObjectName("numBtn_2")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(200, 320, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #8F8C75;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.addBtn.setObjectName("addBtn")
        self.subtractBtn = QtWidgets.QPushButton(self.centralwidget)
        self.subtractBtn.setGeometry(QtCore.QRect(200, 260, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.subtractBtn.setFont(font)
        self.subtractBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #8F8C75;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.subtractBtn.setObjectName("subtractBtn")
        self.plusminBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plusminBtn.setGeometry(QtCore.QRect(20, 380, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.plusminBtn.setFont(font)
        self.plusminBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #6d6d6d;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #FFCC63;\n"
"}")
        self.plusminBtn.setObjectName("plusminBtn")
        self.equalsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.equalsBtn.setGeometry(QtCore.QRect(200, 380, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.equalsBtn.setFont(font)
        self.equalsBtn.setStyleSheet("QPushButton {\n"
"       color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 23px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FCC147, stop:1 #B9800D);\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #262729;\n"
"    background-color: #5A5A5B;\n"
"}")
        self.equalsBtn.setObjectName("equalsBtn")
        self.numBtn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.numBtn_0.setGeometry(QtCore.QRect(80, 380, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.numBtn_0.setFont(font)
        self.numBtn_0.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #c1c1c1;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #8F8C75;\n"
"}")
        self.numBtn_0.setObjectName("numBtn_0")
        self.decimalBtn = QtWidgets.QPushButton(self.centralwidget)
        self.decimalBtn.setGeometry(QtCore.QRect(140, 380, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.decimalBtn.setFont(font)
        self.decimalBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #6d6d6d;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #FFCC63;\n"
"}")
        self.decimalBtn.setObjectName("decimalBtn")
        self.squareBtn = QtWidgets.QPushButton(self.centralwidget)
        self.squareBtn.setGeometry(QtCore.QRect(80, 140, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.squareBtn.setFont(font)
        self.squareBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #6d6d6d;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.squareBtn.setObjectName("squareBtn")
        self.percentBtn = QtWidgets.QPushButton(self.centralwidget)
        self.percentBtn.setGeometry(QtCore.QRect(140, 140, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.percentBtn.setFont(font)
        self.percentBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #6d6d6d;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.percentBtn.setObjectName("percentBtn")
        self.divideBtn = QtWidgets.QPushButton(self.centralwidget)
        self.divideBtn.setGeometry(QtCore.QRect(200, 140, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.divideBtn.setFont(font)
        self.divideBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #8F8C75;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.divideBtn.setObjectName("divideBtn")
        self.squareNBtn = QtWidgets.QPushButton(self.centralwidget)
        self.squareNBtn.setGeometry(QtCore.QRect(20, 140, 46, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.squareNBtn.setFont(font)
        self.squareNBtn.setStyleSheet("QPushButton {\n"
"       background-color: transparent;\n"
"    border: none;\n"
"    color: #6d6d6d;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #45d5eb;\n"
"}")
        self.squareNBtn.setObjectName("squareNBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.displayRes.setText(_translate("MainWindow", "0"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))
        self.factorialBtn.setText(_translate("MainWindow", "x!"))
        self.invmultiplyBtn.setText(_translate("MainWindow", "1/x"))
        self.logBtn.setText(_translate("MainWindow", "log(x)"))
        self.numBtn_7.setText(_translate("MainWindow", "7"))
        self.numBtn_8.setText(_translate("MainWindow", "8"))
        self.numBtn_9.setText(_translate("MainWindow", "9"))
        self.multiplyBtn.setText(_translate("MainWindow", "*"))
        self.numBtn_3.setText(_translate("MainWindow", "3"))
        self.numBtn_1.setText(_translate("MainWindow", "1"))
        self.numBtn_4.setText(_translate("MainWindow", "4"))
        self.numBtn_5.setText(_translate("MainWindow", "5"))
        self.numBtn_6.setText(_translate("MainWindow", "6"))
        self.numBtn_2.setText(_translate("MainWindow", "2"))
        self.addBtn.setText(_translate("MainWindow", "+"))
        self.subtractBtn.setText(_translate("MainWindow", "-"))
        self.plusminBtn.setText(_translate("MainWindow", "+/-"))
        self.equalsBtn.setText(_translate("MainWindow", "="))
        self.numBtn_0.setText(_translate("MainWindow", "0"))
        self.decimalBtn.setText(_translate("MainWindow", "."))
        self.squareBtn.setText(_translate("MainWindow", "x^2"))
        self.percentBtn.setText(_translate("MainWindow", "%"))
        self.divideBtn.setText(_translate("MainWindow", "/"))
        self.squareNBtn.setText(_translate("MainWindow", "x^n"))

