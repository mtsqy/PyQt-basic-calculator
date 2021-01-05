# from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow
import sys

app = QApplication(sys.argv)
calculator = CalculatorWindow()
sys.exit(app.exec_()) 