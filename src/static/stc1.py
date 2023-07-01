from src.db.db_external_pro import Db_Ex_pro





#? LIST PART
surah_options=["Kuaran","Alfabetik","Nuzül"]





#? DATABASE PART
db = Db_Ex_pro("Kuran.db")
all_ayat_list = db.get_element("Ayat", column="ayat_no,surah_id,page")
db.end_process()
del db



#? SETTING PART
#TODO: add windows support
Ayat_f="/tmp/Ayat_Audio"



#? GLOBAL VARIABLES PART
crt_Ayat_i=0
Ayat_dif=0