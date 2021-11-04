# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrappingform.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 389)
        MainWindow.setStyleSheet("*{\n"
"\n"
"    font-family:century gothic;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton{\n"
"    background:red;\n"
"    border-radius:60px\n"
"    \n"
"}\n"
"QToolButton{\n"
"    background:#FFF;\n"
"    border-radius:30px\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
"    color:black;\n"
"}\n"
"QPushButton{\n"
"    color:#FFF;\n"
"    border-radius:15px;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    color:#FFF;\n"
"    background-color: rgb(16, 36, 212);\n"
"}\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    color:rgb(171, 171, 171);\n"
"    border:none;\n"
"    border-bottom: 1px solid rgb(171, 171, 171);\n"
"\n"
"\n"
"}\n"
"#pushButton{\n"
"    background-color:grey;\n"
"}\n"
"#pushButton:hover{\n"
"    background-color:green;\n"
"}\n"
"#pushButton_3{\n"
"    background-color:grey;\n"
"}\n"
"#pushButton_3:hover{\n"
"    background-color:red\n"
"}\n"
"#pushButton_2{\n"
"    background-color:grey;\n"
"}\n"
"#pushButton_2:hover{\n"
"    background-color:blue;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 110, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 120, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        #font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 190, 186, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        #font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 190, 201, 31))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 190, 186, 31))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 310, 621, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter the url"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.label_2.setText(_translate("MainWindow", "Scrapping"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Check Data"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
