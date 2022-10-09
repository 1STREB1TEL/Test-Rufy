from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

app = QApplication([])
window = QWidget()
window.setWindowTitle("Тест Руфи")
window.resize(500, 500)

window.show()
app.exec_()