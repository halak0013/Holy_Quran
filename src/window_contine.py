from src.window import MainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette, QIcon, QTransform, QFont, QIntValidator
from PySide6.QtWidgets import *
# from src.db.db_external_pro import Db_Ex_pro

import src.static.stc1 as st
from src import player as pl

from src.custom_widgets.Ayat_label import Ayat_label
from src.custom_widgets.Btn_ico import Btn_ico
from src.theme import co,set_custom_theme



class Window(MainWindow):
    def __init__(self):
        super().__init__()
        self.tool_part()

    def all_variables(self):
        super().all_variables()

        self.vBox_Surah_search = QVBoxLayout()
        self.hBox_Surah_name = QHBoxLayout()
        self.hBox_Surah_search = QHBoxLayout()
        self.vBox_spacial_search = QVBoxLayout() 

        self.cmb_Surah_name = QComboBox()
        self.cmb_Surah_option = QComboBox()
        self.cmb_fihrist = QComboBox() # TODO: find fihrist translation
        
        self.spn_Ayat = QSpinBox()
        self.lb_fihrist = QLabel("Fihrist")
        self.cmb_theme = QComboBox()
        self.btn_Surah_search = Btn_ico(icon_path="data/img/icons/search.svg")

    def tool_part(self):
        self.hBox_Surah_name.addWidget(self.cmb_Surah_name)
        self.hBox_Surah_name.addWidget(self.cmb_Surah_option)
        self.hBox_Surah_search.addWidget(self.spn_Ayat)
        self.hBox_Surah_search.addWidget(self.btn_Surah_search)
        self.vBox_spacial_search.addWidget(self.lb_fihrist)
        self.vBox_spacial_search.addWidget(self.cmb_fihrist)
        self.vBox_spacial_search.setAlignment(Qt.AlignTop)

        self.vBox_spacial_search.setSpacing(30)
        self.vBox_tools.setSpacing(30)
        
        
        self.vBox_Surah_search.addLayout(self.hBox_Surah_name)
        self.vBox_tools.addLayout(self.vBox_Surah_search)
        self.vBox_tools.addLayout(self.hBox_Surah_search)
        self.vBox_tools.addLayout(self.vBox_spacial_search)
        

        self.cmb_Surah_option.addItems(st.surah_options)
        self.spn_Ayat.setMinimum(1)
        self.fill_fihrist()

        self.cmb_Surah_name.currentIndexChanged.connect(self.cmb_Surah_change)
        self.spn_Ayat.valueChanged.connect(self.Ayat_chage)
        self.cmb_Surah_option.currentIndexChanged.connect(self.Surah_opt_chage)
        self.btn_Surah_search.clicked.connect(self.btn_Surah_search_clicked)

        self.search_part()
        
        self.cmb_theme.currentIndexChanged.connect(self.cmb_change_theme)
        self.cmb_theme.addItems(["Koyu Tema","Açık Tema"])
        self.vBox_tools.addWidget(self.cmb_theme)
    def search_part(self):
        self.get_Surah_name()
        
        self.editable_combo(self.cmb_Surah_name)
        self.editable_combo(self.cmb_fihrist)
        
        self.cmb_fihrist.currentIndexChanged.connect(self.cmb_fihrist_change)

    def Surah_opt_chage(self):
        self.get_Surah_name()

    def get_Surah_name(self):
        index = self.cmb_Surah_option.currentIndex()
        if index != 2:
            st.Surah_names.sort(key=lambda x: x[index])
        else:
            st.Surah_names.sort(key=lambda x: x[3])

        self.cmb_Surah_name.clear()
        for s in st.Surah_names:
            self.cmb_Surah_name.addItem(f"{s[0]}-{s[1]}")
            
            
            
    def fill_fihrist(self):
        self.db.start()
        self.fihrist_list = self.db.get_element("FihristList","word_id,text")
        self.db.end_process()
        self.cmb_fihrist.addItems([fl[1] for fl in self.fihrist_list])
        
            
            
            

    def btn_Surah_search_clicked(self):
        selected = self.cmb_page_option.currentIndex()
        surah = self.cmb_Surah_name.currentText().split("-")[0]
        ayat = self.spn_Ayat.value()
        print(ayat,surah)
        self.db.start()
        page = self.db.get_element("Ayat", column="ayat_id,page",
                                    where=("ayat_no", "surah_id"), data=(ayat, surah))
        self.db.end_process()
        print(page)
        st.crt_Ayat_i=page[0][0]-1
        if selected == 0:
            self.spn_num.setValue(page[0][1]+1)
        else:
            self.spn_num.setValue(surah)
        self.Ayat_coloring()
            
    def Ayat_chage(self):
        pass
    
    def cmb_Surah_change(self):
        surah = self.cmb_Surah_name.currentText().split("-")[0]
        self.db.start()
        max_ayat = self.db.get_element("Surahs", column="ayat_count",where=("surah_id",), data=(surah,))[0][0]
        self.db.end_process()
        print(max_ayat)
        self.spn_Ayat.setMaximum(max_ayat)
        
    def cmb_fihrist_change(self):
        index=self.cmb_fihrist.currentIndex()
        word_id=self.fihrist_list[index][0]
        self.db.start()
        ayats = self.db.get_element("FihristAyat",where=("word_id",), data=(word_id,))
        ayat_info=list(map(lambda x: (x[0],x[2]),ayats))
        self.all_ayat=[]
        for a in ayat_info:
            self.all_ayat.append(self.db.get_element("Ayat",where=("ayat_no","surah_id"),data=a)[0])
        #print(self.all_ayat)
        self.fill_page(is_special=True)
        
        self.db.end_process()
        
        
        
    def editable_combo(self,cmb):
        cmb.setEditable(True)
        completer = QCompleter(cmb.model(), self)
        completer.setFilterMode(Qt.MatchContains)  # Klavyeden yazılan kısmın elemanların herhangi bir yerinde geçmesi için
        completer.setCaseSensitivity(Qt.CaseInsensitive) # Büyük küçük harf hassasiyetini kapatarak aramayı yapar
        cmb.setCompleter(completer)
        
    def cmb_change_theme(self):
        index=self.cmb_theme.currentIndex()
        if index==0:
            co.dark_theme()
        else:
            co.light_theme()
        set_custom_theme(QApplication.instance())
        
