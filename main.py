import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
janela = QWidget()
janela.show()
sys.exit(app.exec_)