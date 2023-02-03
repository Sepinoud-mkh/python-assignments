from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def sum():
app=QApplication([])        #ورودی این تابع یک لیست میشه

loader=QUiLoader()
window=loader.load("calculator.ui")
window.show()

window.sum.clicked.connect(sum)
window.
app.exec()