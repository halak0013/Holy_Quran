import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette,QIcon
from PySide6.QtWidgets import *
from db.db_external_pro import Db_Ex_pro
import static.stc1 as st
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
        self.db=Db_Ex_pro("Kuran.db")
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
        self.btn_play=QPushButton("⏯️")
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
        
    #? layout adding part
    def layout_add(self):
        self.vBox_main.addLayout(self.hBox_header)
        self.vBox_main.addWidget(self.splitter)
        self.header_part()
        self.tool_part()
        
        
    def header_part(self):
        self.hBox_header.addWidget(self.btn_setting)
        self.hBox_header.addWidget(self.btn_play_back)
        self.hBox_header.addWidget(self.btn_play)
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
        self.get_Surah_name()
        
        
    def get_Surah_name(self):
        self.Surah_names=self.db.get_element("Surahs")
        #TODO: add Surah name item limit
        print(self.Surah_names)
        for s in self.Surah_names:
            self.cmb_Surah_name.addItem(f"{s[0]}-{s[1]}")
        self.cmb_Surah_option.addItems(st.surah_options)
        
    #? splitter part
    def splitter_part(self):
        # Ana bölünür paneli oluştur
        self.splitter.addWidget(self.wdg_tools)
        self.splitter.addWidget(self.wdg_Ayat)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
