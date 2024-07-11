from src.db.db_external_pro import Db_Ex_pro
import locale
from locale import gettext as _
import os
# Translation Constants:
APPNAME = "holy-quran"
TRANSLATIONS_PATH = "/usr/share/locale"
SYSTEM_LANGUAGE = os.environ.get("LANG")

# Translation functions:
locale.bindtextdomain(APPNAME, TRANSLATIONS_PATH)
locale.textdomain(APPNAME)
locale.setlocale(locale.LC_ALL, SYSTEM_LANGUAGE)


class stc:
    # ? LIST PART
    surah_options = [_("Quran"), _("Alphabetical"), _("Nuzul")]
    print(surah_options)

    # ? DATABASE PART
    db = Db_Ex_pro("Kuran.db")
    all_ayat_list = db.get_element("Ayat", column="ayat_no,surah_id,page")
    db.end_process()

    db.start()
    Surah_names = db.get_element("Surahs")
    db.end_process()

    del db


    # ? SETTING PART
    # TODO: add windows support
    home_directory = os.path.expanduser("~")
    App_dir = home_directory + "/.Holy_Quran"
    app_config = App_dir + "/config"
    Ayat_f = App_dir + "/Ayat_Audio"


    # ? GLOBAL VARIABLES PART
    crt_Ayat_i = 0
    Ayat_dif = 0

    spn_p_min = 0
    spn_p_max = 604
    spn_s_min = 1
    spn_s_max = 114


    def __init__(self):
        pass
