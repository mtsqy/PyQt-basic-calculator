from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from calculator import CalculatorWindow
import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()
    calculator = CalculatorWindow()
    sys.exit(appctxt.app.exec_()) 