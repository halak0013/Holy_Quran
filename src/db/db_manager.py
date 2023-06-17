import sqlite3


class Db_manager():
    def __init__(self,dbpath):
        # Database connection
        self.conn = sqlite3.connect(f'{dbpath}')
        self.cursor = self.conn.cursor()

        # Generate Surahs Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Surahs (
                            surah_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            surah_name TEXT NOT NULL,
                            ayat_count INTEGER,
                            nuzul_sort INTEGER
                            )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Imams (
                            imam_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            imam_name TEXT NOT NULL,
                            imam_code TEXT NOT NULL
                            )''')

        # Generate Surahs Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Ayat (
                            ayat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ayat_no INTEGER NOT NULL,
                            ayat TEXT,
                            surah_id INTEGER,
                            is_secde_ayat INTEGER,
                            page INTEGER NOT NULL,
                            FOREIGN KEY (surah_id) REFERENCES Surahs(surah_id)
                            )''')

    def add_surah(self, surah_name: str, ayat_count: int, nuzul_sort: int):
        self.conn = sqlite3.connect('Kuran.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "INSERT INTO Surahs (surah_name, ayat_count, nuzul_sort) VALUES (?, ?, ?)", (surah_name, ayat_count, nuzul_sort))
        self.conn.commit()
        #print("Added Surah")
        
    def add_imam(self, imam_name: str, imam_code: str):
        self.conn = sqlite3.connect('Kuran.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "INSERT INTO Imams (imam_name, imam_code) VALUES (?, ?)", (imam_name, imam_code))
        self.conn.commit()
        #print("Added imam")
        

    def add_ayat(self, ayat_no, ayat, surah_id, is_secde_ayat,page):
        self.conn = sqlite3.connect('Kuran.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO Ayat (ayat_no, ayat, surah_id, page, is_secde_ayat) VALUES (?, ?, ?, ?, ?)",
                            (ayat_no, ayat, surah_id, is_secde_ayat, page))
        self.conn.commit()
        #print("Ayet eklendi.")
        

    def delete_ayat(self, ayat_id):
        self.conn = sqlite3.connect('Kuran.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM Ayat WHERE ayat_id = ?", (ayat_id,))
        self.conn.commit()
        print("Deleted ayat.")
        

    def list_Surah(self):
        self.conn = sqlite3.connect('Kuran.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Surahs")
        sure = self.cursor.fetchall()
        for kategori in sure:
            print(
                f"Sure ID: {kategori[0]}, Sure Adı: {kategori[1]}, Ayet sayısı: {kategori[2]},, Nuzul sırası: {kategori[3]}")
        


    def end_process(self):
        # Close database connection
        #self.conn.commit()
        self.conn.close()
        



if __name__ == "main":
    # Kategori ekleme işlemi
    Db_manager.add_surah("Fatiha", 7, 5)
    Db_manager.add_surah("Bakar", 286, 87)

    # Ürün ekleme işlemi
    Db_manager.add_ayat(1, "Rahman ve Rahim olan Allah'ın adıyla", 1, 0)
    Db_manager.add_ayat(1, "Rahman ve Rahim olan Allah'ın adıyla", 1, 0)
    Db_manager.add_ayat(1, "Rahman ve Rahim olan Allah'ın adıyla", 1, 0)
    Db_manager.add_ayat(1, "Rahman ve Rahim olan Allah'ın adıyla", 1, 0)
    Db_manager.add_ayat(1, "Rahman ve Rahim olan Allah'ın adıyla", 1, 0)

    # Ürün silme işlemi
    # delete_ayat(1)

    # Kategorileri listeleme işlemi
    Db_manager.list_Surah()

    # Ürünleri listeleme işlemi
    Db_manager.list_Ayat()
