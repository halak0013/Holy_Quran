import sys
from src.window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("data/img/logo57_57.png"))
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())