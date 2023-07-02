from PySide6.QtWidgets import QPushButton
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtGui import QPixmap,QPainter,QIcon
from PySide6.QtCore import Qt

class Btn_ico(QPushButton):
    def __init__(self,text:str="",icon_path=""):
        super().__init__(text)
        if ".png" in icon_path:
            icon=QIcon(icon_path)
            self.setIcon(icon)
        elif ".svg" in icon_path:
            try:
                renderer = QSvgRenderer(icon_path)
                pixmap = QPixmap(24, 24)
                pixmap.fill(Qt.transparent)
                painter = QPainter(pixmap)
                renderer.render(painter)
                painter.end()
                self.setIcon(QIcon(pixmap))
            except Exception as e:
                print(e.with_traceback)
        