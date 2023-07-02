from src.db.db_external_pro import Db_Ex_pro





#? LIST PART
surah_options=["Kuran","Alfabetik","Nuzül"]





#? DATABASE PART
db = Db_Ex_pro("Kuran.db")
all_ayat_list = db.get_element("Ayat", column="ayat_no,surah_id,page")
db.end_process()

db.start()
Surah_names = db.get_element("Surahs")
db.end_process()

del db


#? SETTING PART
#TODO: add windows support
Ayat_f="/tmp/Ayat_Audio"



#? GLOBAL VARIABLES PART
crt_Ayat_i=0
Ayat_dif=0

spn_p_min=1
spn_p_max=604
spn_s_min=1
spn_s_max=114