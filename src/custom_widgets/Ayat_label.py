from PySide6.QtWidgets import QLabel,QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Signal

class Ayat_label(QLabel):
    clicked=Signal(tuple,int)
    
    def __init__(self,text,ayat_info:tuple,index:int):
        super().__init__(text)
        self.index=index
        self.ayat_info=ayat_info
        
        self.setWordWrap(True)
        self.setFont(QFont("Shaikh Hamdullah Mushaf", 23, weight=3))
        
    def mousePressEvent(self,event):
        self.clicked.emit(self.ayat_info,self.index)
        #self.setStyleSheet("QLabel {color:red;}")
        super().mousePressEvent(event)
        #self.chageCurrentColor()

    def chageCurrentColor(self):
        # Get the currently selected label (if any)
        current_label = self.window().selected_label
        
        # Restore the color of the previously selected label (if any)
        if current_label:
            current_label.setStyleSheet("QLabel { color: white; }")
        
        # Set the color of the clicked label
        self.setStyleSheet("QLabel { color: red; }")
        
        # Set the clicked label as the currently selected label
        self.window().selected_label = self
