import sys

from PySide2.QtWidgets import QApplication

from pswgendlg import PswGenDialog


app = QApplication([])

win = PswGenDialog()
win.show()

sys.exit(app.exec_())
