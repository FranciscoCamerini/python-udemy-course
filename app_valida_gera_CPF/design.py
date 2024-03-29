from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_centralWidget(object):
    def setupUi(self, centralWidget):
        centralWidget.setObjectName("centralWidget")
        centralWidget.resize(786, 231)
        self.centralwidget = QtWidgets.QWidget(centralWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelRetorno = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.labelRetorno.setFont(font)
        self.labelRetorno.setText("")
        self.labelRetorno.setObjectName("labelRetorno")
        self.gridLayout.addWidget(self.labelRetorno, 3, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.btnGeraCPF = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnGeraCPF.setFont(font)
        self.btnGeraCPF.setObjectName("btnGeraCPF")
        self.gridLayout.addWidget(self.btnGeraCPF, 1, 3, 1, 1)
        self.inputValidaCPF = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.inputValidaCPF.setFont(font)
        self.inputValidaCPF.setObjectName("inputValidaCPF")
        self.gridLayout.addWidget(self.inputValidaCPF, 0, 1, 1, 2)
        self.btnValidaCPF = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnValidaCPF.setFont(font)
        self.btnValidaCPF.setObjectName("btnValidaCPF")
        self.gridLayout.addWidget(self.btnValidaCPF, 0, 3, 1, 1)
        centralWidget.setCentralWidget(self.centralwidget)

        self.retranslateUi(centralWidget)
        QtCore.QMetaObject.connectSlotsByName(centralWidget)

    def retranslateUi(self, centralWidget):
        _translate = QtCore.QCoreApplication.translate
        centralWidget.setWindowTitle(_translate("centralWidget", "Valida ou Gera CPF"))
        self.label_2.setText(_translate("centralWidget", "Validar CPF"))
        self.label.setText(_translate("centralWidget", "GERA CPF"))
        self.btnGeraCPF.setText(_translate("centralWidget", "GERAR"))
        self.btnValidaCPF.setText(_translate("centralWidget", "VALIDAR"))
