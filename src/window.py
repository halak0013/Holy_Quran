import locale
from locale import gettext as _


from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from src.db.db_external_pro import Db_Ex_pro
from src.static.stc1 import stc as st
from src import player as pl
from src.custom_widgets.Ayat_label import Ayat_label
from src.theme import co



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ? Main Part
        self.setWindowTitle(_("Holy Quran"))
        self.resize(1000, 1100)
        self.all_variables()
        self.layout_add()

        self.splitter_part()

        self.setCentralWidget(self.wdg_main)

        self.fill_page(("page",), (0,))
        self.change_Surah_name()

    def all_variables(self):
        self.imam_code = "Abu_Bakr_Ash-Shaatree_64kbps"
        self.play_status = "none"
        self.sellected_ayat: tuple

        self.db = Db_Ex_pro("Kuran.db")
        self.splitter = QSplitter(Qt.Horizontal)

        self.wdg_main = QWidget()
        self.wdg_header = QWidget()
        self.wdg_tools = QWidget()
        self.wdg_Ayat = QWidget()
        self.wdg_Ayat_player = QWidget()
        self.wdg_player = QWidget()

        self.vBox_main = QVBoxLayout(self.wdg_main)
        self.hBox_header = QHBoxLayout()
        self.vBox_tools = QVBoxLayout(self.wdg_tools)
        self.vBox_Ayat = QVBoxLayout()
        self.vBox_Ayat_player = QVBoxLayout(self.wdg_Ayat_player)
        self.hBox_player = QHBoxLayout()

        self.scroll_Ayat = QScrollArea()

        self.scroll_Ayat.setWidgetResizable(True)
        self.scroll_Ayat.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_Ayat.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scroll_Ayat.setWidget(self.wdg_Ayat)

        self.btn_setting = QPushButton(_("⚙ Holy Quran"))
        self.cmb_page_option = QComboBox()
        self.label_Surah_name = QLabel("Fatiha")
        self.btn_page_next = QPushButton("◀️")
        self.spn_num = QSpinBox()
        self.btn_page_back = QPushButton("▶️")

        self.btn_play_back = QPushButton("⏪")
        self.btn_play = QPushButton("⏯️")
        self.btn_play_next = QPushButton("⏩")
        self.cmb_imams = QComboBox()

    # ? layout adding part
    def layout_add(self):
        self.vBox_main.addLayout(self.hBox_header)
        self.vBox_main.addWidget(self.splitter)
        self.header_part()
        self.Ayat_part()
        self.player_part()

    def header_part(self):
        self.hBox_header.addWidget(self.btn_setting)
        self.hBox_header.addWidget(self.cmb_page_option)
        self.hBox_header.addWidget(self.label_Surah_name)
        self.hBox_header.addWidget(self.btn_page_next)
        self.hBox_header.addWidget(self.spn_num)
        self.hBox_header.addWidget(self.btn_page_back)

        self.cmb_page_option.addItems([_("Page"), _("Surah")])
        self.cmb_page_option.currentIndexChanged.connect(
            self.cmb_change_page_option)

        self.spn_num.setMinimum(st.spn_p_min)
        self.spn_num.setMaximum(st.spn_p_max)
        self.spn_num.valueChanged.connect(self.spn_num_change)

        self.btn_setting.clicked.connect(self.btn_clk_setting)
        self.btn_play_back.clicked.connect(self.btn_clk_play_back)
        self.btn_play.clicked.connect(self.btn_clk_play)
        self.btn_play_next.clicked.connect(self.btn_clk_play_next)
        self.btn_page_back.clicked.connect(self.btn_clk_back)
        self.btn_page_next.clicked.connect(self.btn_clk_next)

    def Ayat_part(self):
        self.scroll_Ayat.setMinimumSize(500, 700)
        self.wdg_Ayat.setLayout(self.vBox_Ayat)
        self.vBox_Ayat_player.addWidget(self.scroll_Ayat)

    def player_part(self):
        self.hBox_player.addWidget(self.btn_play_back)
        self.hBox_player.addWidget(self.btn_play)
        self.hBox_player.addWidget(self.btn_play_next)
        self.hBox_player.addWidget(self.cmb_imams)
        self.db.start()
        self.imam_list = self.db.get_element("Imams", "imam_name,imam_code")
        self.db.end_process()
        self.cmb_imams.addItems([il[0] for il in self.imam_list])
        self.cmb_imams.currentIndexChanged.connect(self.imam_chaged)

        self.vBox_Ayat_player.addLayout(self.hBox_player)

    # ? fill pages
    def fill_page(self, where=(), data=(), is_special=False):
        if not is_special:
            self.db.start()
            self.all_ayat = self.db.get_element("Ayat", where=where, data=data)
            self.db.end_process()

        while self.vBox_Ayat.count():
            item = self.vBox_Ayat.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        firs_id = self.all_ayat[0][0]-1  # ? all ayat_id = index +1
        st.Ayat_dif = firs_id
        # 0     1   2   3 differance 122
        # 122 123 124 125

        tmp_index = firs_id
        self.ayat_list = []
        for a in self.all_ayat:
            ayat = Ayat_label(str(a[2]), a, tmp_index)
            ayat.clicked.connect(self.Ayat_clicked)
            self.ayat_list.append(ayat)
            tmp_index += 1

            ayrac = QFrame()
            ayrac.setFrameShape(QFrame.HLine)

            self.vBox_Ayat.addWidget(ayat)
            self.vBox_Ayat.addWidget(ayrac)

    def Ayat_clicked(self, info, index):
        st.crt_Ayat_i = index
        self.Ayat_coloring()
        print(st.crt_Ayat_i)
        self.play_status = "none"
        pl.stopAudio()

    def Ayat_coloring(self):
        index = st.crt_Ayat_i-st.Ayat_dif
        print(
            f"index: {index} crt_Ayat_i: {st.crt_Ayat_i} st.Ayat_dif: {st.Ayat_dif}")
        if index >= len(self.ayat_list):
            self.btn_clk_next()
            self.Ayat_coloring()
            return
        elif index < 0:
            self.btn_clk_back()
            self.Ayat_coloring()
            return
        for a in self.ayat_list:
            a.setStyleSheet(f"QLabel {{ color: {co.seconder_color} ; }}")
            if a.ayat_info[4] == 1:
                a.setStyleSheet(f"QLabel {{ color: {co.highlight_color}; }}")
        self.scroll_Ayat.ensureWidgetVisible(self.ayat_list[index])
        self.ayat_list[index].setStyleSheet(
            "QLabel { color: red; }")
        # self.scroll_Ayat.verticalScrollBar().setPageStep(5)

    # ? splitter part

    def splitter_part(self):
        # Ana bölünür paneli oluştur
        self.splitter.addWidget(self.wdg_tools)
        self.splitter.addWidget(self.wdg_Ayat_player)

    def change_page(self):
        self.fill_page(("page",), (self.spn_num.value(),))

    def change_Surah(self):
        self.fill_page(("surah_id",), (self.spn_num.value(),))

    def cmb_change_page_option(self):
        selected = self.cmb_page_option.currentIndex()
        if selected == 0:
            self.spn_num.setMinimum(st.spn_p_min)
            self.spn_num.setMaximum(st.spn_p_max)
            self.change_page()
            print(selected)
        else:
            self.spn_num.setMinimum(st.spn_s_min)
            self.spn_num.setMaximum(st.spn_s_max)
            self.change_Surah()
            print(selected)

    def imam_chaged(self):
        self.imam_code = self.imam_list[self.cmb_imams.currentIndex()][1]
        pl.stopAudio()
        self.play_status = "none"

    def change_Surah_name(self):
        index = self.all_ayat[0][3]-1
        self.label_Surah_name.setText(
            f"{st.Surah_names[index][0]}-{st.Surah_names[index][1]}")

    def spn_num_change(self):
        selected = self.cmb_page_option.currentIndex()
        if selected == 0:
            self.change_page()
        else:
            self.change_Surah()
        self.change_Surah_name()

    def btn_clk_setting(self):
        pass

    def btn_clk_play_back(self):
        pl.is_first = True
        st.crt_Ayat_i -= 1
        self.Ayat_coloring()
        sellected_ayat = st.all_ayat_list[st.crt_Ayat_i]
        pl.playAudio(sellected_ayat)

    def btn_clk_play(self):
        # ? Ayat, Surah, Page
        print(self.play_status)
        pl.imam = self.imam_code
        pl.slf = self
        sellected_ayat = st.all_ayat_list[st.crt_Ayat_i]
        print(sellected_ayat)
        if self.play_status == "none":
            self.play_status = "playing"
            pl.playAudio(
                sellected_ayat)
        elif self.play_status == "playing":
            self.play_status = "pause"
            pl.pause_audio()
        else:
            self.play_status = "playing"
            pl.unPaues_audio()
        surah_options = [_("Quran"), _("Alphabetical"), _("Nuzul")]
        print(surah_options)

    def btn_clk_play_next(self):
        pl.is_first = True
        st.crt_Ayat_i += 1
        self.Ayat_coloring()
        sellected_ayat = st.all_ayat_list[st.crt_Ayat_i]
        pl.playAudio(sellected_ayat)

    def btn_clk_back(self):
        # ? it is already changing in the spinner function
        self.spn_num.setValue(self.spn_num.value()-1)

    def btn_clk_next(self):
        # ? it is already changing in the spinner function
        self.spn_num.setValue(self.spn_num.value()+1)
