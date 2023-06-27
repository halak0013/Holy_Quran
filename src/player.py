import sys
import os
import pygame
from PyQt6.QtCore import QTimer
import requests
from src.db.db_external_pro import Db_Ex_pro


class Player_c:
    def __init__(self):
        pygame.mixer.init()
        self.db = Db_Ex_pro("Kuran.db")
        self.imam="Abu_Bakr_Ash-Shaatree_64kbps"

        self.global_index=0
        self.current_index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.handleEndEvent)
        
        self.audio_files=[]
        
        #? it gets all ayat data (ayat_no,surah_id,page)
        self.all_ayat_list = self.db.get_element( "Ayat", column="ayat_no,surah_id,page",
                        where="where ayat_no IS NOT ?",data=(-1,),is_special=True)


    def play_audio(self,track,imam="Abu_Bakr_Ash-Shaatree_64kbps"):
        #? it download 5 Ayat for the first time
        self.global_index=self.all_ayat_list.index(track)
        self.download_audio(self.all_ayat_list[self.global_index:self.global_index+5])
        self.global_index+=5
        self.imam=imam
        
        pygame.mixer.music.load(self.audio_files[self.current_index])
        pygame.mixer.music.play()
        self.timer.start(100)  # it contol status

    def pause_audio(self):
        pygame.mixer.pause()

    def unPaues_audio(self):
        pygame.mixer.unpause()

    def stop_audio(self):
        pygame.mixer.stop()
        self.timer.stop()

    def download_audio(self, tracks:list):
        if not os.path.exists("/tmp/Ayat_Audio"):
            os.makedirs("/tmp/Ayat_Audio")
        for t in tracks:
            trc=self.convert_to_file(t)
            if os.path.exists(f"/tmp/Ayat_Audio/{trc[0]}"):
                self.audio_files.append(f"/tmp/Ayat_Audio/{trc[0]}")
                continue
            try:
                response = requests.get(trc[1])
                response.raise_for_status()  # İndirme başarısız olursa hata fırlatır
                with open(f"/tmp/Ayat_Audio/{trc[0]}", 'wb') as dosya:
                    dosya.write(response.content)
                self.audio_files.append(f"/tmp/Ayat_Audio/{trc[0]}")
                print("Dosya başarıyla indirildi.")
            except requests.exceptions.HTTPError as errh:
                print("HTTP Hatası:", errh)
            except requests.exceptions.ConnectionError as errc:
                print("Bağlantı Hatası:", errc)
            except requests.exceptions.Timeout as errt:
                print("Zaman Aşımı Hatası:", errt)
            except requests.exceptions.RequestException as err:
                print("Bağlantı Hatası:", err)

    def convert_to_file(self,track):
        #* https://everyayah.com/data/Abdul_Basit_Murattal_64kbps/001002.mp3
        
        file="{:03d}".format(track[1])+"{:03d}".format(track[0])+".mp3"
        url="https://everyayah.com/data/"+self.imam+"/"+file
        return (file, url)


    def handleEndEvent(self):
        if not pygame.mixer.music.get_busy():#? audio processing is finished
            self.current_index += 1
            self.global_index += 1
            
            t = self.all_ayat_list[self.global_index]
            trc=self.convert_to_file(t)
            if not os.path.exists(f"/tmp/Ayat_Audio/{trc[0]}"):
                self.audio_files.append(f"/tmp/Ayat_Audio/{trc[0]}")
                self.download_audio([t,])
                
            if self.current_index < len(self.audio_files):
                self.play_audio()
            else:
                self.stop_audio()
