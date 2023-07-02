import sys
from src.window_contine import Window
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Arial"))
    app.setWindowIcon(QIcon("data/img/logo57_57.png"))
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec())