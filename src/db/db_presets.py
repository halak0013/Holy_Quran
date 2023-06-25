INT_PKA = "INTEGER PRIMARY KEY AUTOINCREMENT"
INT = "INTEGER"
TX = "TEXT"
NN = "NOT NULL"



surah_table = [f"surah_id {INT_PKA}", f"surah_name {TX} {NN}",
               f"ayat_count {INT}", f"nuzul_sort {INT}"
               ]
surah_table_c = ["surah_id", "surah_name", "ayat_count", "nuzul_sort"]

ayat_table = [f"ayat_id {INT_PKA}", f"ayat_no {INT} {NN}",
              f"ayat {TX}", f"surah_id {INT}", f"is_secde_ayat {INT}",
              f"page {INT} {NN}", "FOREIGN KEY (surah_id) REFERENCES Surahs(surah_name)"
              ]
ayat_table_c = ["ayat_id", "ayat_no", "ayat",
                "surah_id", "is_secde_ayat", "page"]


