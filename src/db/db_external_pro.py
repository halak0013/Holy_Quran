import sqlite3
import db_presets
import db_manager


class Db_Ex_pro():
    def __init__(self, dbpath):
        # Database connection
        self.conn = sqlite3.connect(f'{dbpath}')
        self.cursor = self.conn.cursor()

    def generate_table(self, table_name, table_info):
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ('
        len_table = len(table_info)-1

        for i, e in enumerate(table_info):
            if len_table != i:
                query += f"{e}, "
            else:
                query += f"{e}"
        query += ")"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()  # ! çalışmayabilin

    def add_element(self, table_name, data, table_columns):
        self.cursor = self.conn.cursor()
        query = f"INSERT INTO {table_name} ("
        q_mark = "("
        len_c = len(table_columns)-1
        for i, e in enumerate(table_columns):
            if i != len_c:
                query += e+", "
                q_mark += "?, "
            else:
                query += e
                q_mark += "? "
        query += f") VALUES {q_mark})"
        print(query)
        self.cursor.execute(query, data)
        self.conn.commit()

    def delet_element(self, tablo_name, column, data):
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            f"DELETE FROM {tablo_name} WHERE {column} = ?", (data,))
        self.conn.commit()

    def update_element(self, tablo_name, column, up_col, where_col, new_data, where_data):
        self.cursor.execute(
            f"UPDATE {tablo_name} SET {up_col} = ? WHERE {where_col} = ?", (new_data, where_data))
        self.conn.commit()

    def list_Surah(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Surahs")
        sure = self.cursor.fetchall()
        for kategori in sure:
            print(
                f"Sure ID: {kategori[0]}, Sure Adı: {kategori[1]}, Ayet sayısı: {kategori[2]},, Nuzul sırası: {kategori[3]}")

    def get_element(self,table_name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()
    
    def end_process(self):
        self.conn.close()


if __name__ == "__main__":
    print("çalıştı")
    # t=db_manager.Db_manager("ee.db")
    # t.generate_table()
    test = Db_Ex_pro("test.db")
    test.generate_table("meyve", db_presets.ornek_tablo)
    test.add_element(table_name="meyve", data=[
                     "elma"], table_columns=db_presets.ornek_tablo_c)
    test.delet_element("meyve", "name", "elma")
