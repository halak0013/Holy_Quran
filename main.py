#Bismillahirrahmanirrahim
import os

print(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import sys
from src.window_continue import Window
from src.theme import set_custom_theme
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Arial"))
    app.setWindowIcon(QIcon("data/img/holy-quran.png"))
    set_custom_theme(app)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec())