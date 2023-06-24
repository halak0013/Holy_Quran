import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette,QIcon
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #? Main Part
        self.setWindowTitle("Kuran-ı Kerim")
        
        self.all_variables()
        self.layout_add()
        self.splitter_part()


        self.setCentralWidget(self.wdg_main)
        
        


    def all_variables(self):
        self.splitter = QSplitter(Qt.Horizontal)
        
        self.wdg_main=QWidget()
        self.wdg_header=QWidget()
        self.wdg_tools=QWidget()
        self.wdg_Ayat=QWidget()
        
        self.vBox_main=QVBoxLayout(self.wdg_main)
        self.hBox_header=QHBoxLayout()
        self.vBox_tools=QVBoxLayout(self.wdg_tools)
        self.vBox_Ayat=QVBoxLayout(self.wdg_Ayat)
        
        
        self.btn_setting=QPushButton("⚙ Kuran-ı Kerim")
        self.btn_play_back=QPushButton("⏪")
        self.btn_play_back=QPushButton("⏯️")
        self.btn_play_next=QPushButton("⏩")
        self.label_Surah_name=QLabel("Fatih")
        self.btn_page_back=QPushButton("◀️")
        self.label_page_num=QLabel("Sayfa")
        self.btn_page_next=QPushButton("▶️")
        
        self.vBox_Surah_search=QVBoxLayout()
        self.hBox_Surah_name=QHBoxLayout()
        
        self.cmb_Surah_name=QComboBox()
        self.cmb_Surah_option=QComboBox()
        self.inp_Ayat=QLineEdit()
        
        
        
    
    
    def layout_add(self):
        self.vBox_main.addLayout(self.hBox_header)
        self.vBox_main.addWidget(self.splitter)
        self.header_part()
        self.tool_part()
        
        
    def header_part(self):
        self.hBox_header.addWidget(self.btn_setting)
        self.hBox_header.addWidget(self.btn_play_back)
        self.hBox_header.addWidget(self.btn_play_back)
        self.hBox_header.addWidget(self.btn_play_next)
        self.hBox_header.addWidget(self.label_Surah_name)
        self.hBox_header.addWidget(self.btn_page_back)
        self.hBox_header.addWidget(self.label_page_num)
        self.hBox_header.addWidget(self.btn_page_next)
        
    def tool_part(self):
        self.hBox_Surah_name.addWidget(self.cmb_Surah_name)
        self.hBox_Surah_name.addWidget(self.cmb_Surah_option)
        
        self.vBox_Surah_search.addLayout(self.hBox_Surah_name)
        self.vBox_tools.addLayout(self.vBox_Surah_search)
        self.vBox_tools.addWidget(self.inp_Ayat)
        
        self.inp_Ayat.setPlaceholderText("Ayet No")
        
    
    def splitter_part(self):
        # Ana bölünür paneli oluştur
        self.splitter.addWidget(self.wdg_tools)
        self.splitter.addWidget(self.wdg_Ayat)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
