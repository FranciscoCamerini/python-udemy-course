from gerador_cpf import geracpf
from validacpf import validacpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design
import sys


class GeraValidaCPF(QMainWindow, design.Ui_centralWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelRetorno.setText(
            str(geracpf())
        )

    def valida_cpf(self):
        cpf = self.inputValidaCPF.text()
        self.labelRetorno.setText(
            str(validacpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()
