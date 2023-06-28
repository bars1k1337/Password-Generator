import random

from PySide2.QtWidgets import QDialog, QWidget
from PySide2.QtCore import Qt

from ui_pswgendlg import Ui_PswGenDialog


MIN_PASSWORD_LEN = 6
MAX_PASSWORD_LEN = 14


class PswGenDialog(QDialog, Ui_PswGenDialog):
    def __init__(self, parent: QWidget = None, flags: Qt.WindowFlags = Qt.WindowFlags()):
        super(PswGenDialog, self).__init__(parent, flags)
        self.setupUi(self)

        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.letters += self.letters.upper()
        self.digits = "1234567890"
        self.specs = "!@#$%^&*"

        self.pswLenSlider.setRange(MIN_PASSWORD_LEN, MAX_PASSWORD_LEN)
        self.pswLenSpin.setRange(MIN_PASSWORD_LEN, MAX_PASSWORD_LEN)

        self.pswLenSlider.valueChanged.connect(self.pswLenSpin.setValue)
        self.pswLenSpin.valueChanged.connect(self.pswLenSlider.setValue)
        self.generateButton.clicked.connect(self.generatePassword)

    def generatePassword(self):
        def ensureUse(text: str, chars: str) -> str:
            chars_set = set(chars)
            text_set = set(text)
            has_chars = len(text_set.intersection(chars_set)) > 0
            if not has_chars:
                char = random.choice(chars)
                pos = random.randrange(len(text))
                text = text[:pos] + char + text[pos + 1:]
            return text

        chars = self.letters
        if self.useDigitsCheck.isChecked():
            chars += self.digits
        if self.useSpecsCheck.isChecked():
            chars += self.specs

        password = ""
        for n in range(self.pswLenSpin.value()):
            password += random.choice(chars)

        if self.useDigitsCheck.isChecked():
            password = ensureUse(password, self.digits)

        if self.useSpecsCheck.isChecked():
            password = ensureUse(password, self.specs)

        self.pswEdit.setText(password)
