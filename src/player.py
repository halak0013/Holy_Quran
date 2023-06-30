import os
import pygame
import requests
from src.db.db_external_pro import Db_Ex_pro
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QLabel
# TODO: when playing Ayat, it sholud download sound


def playAudio(track):
    if track[0] == -1:
        track=(1, track[1],track[2])
    print(audio_files)
    global pause_status
    pause_status = False
    # ? it download 5 Ayat for the first time
    global global_index
    global is_first
    global_index = all_ayat_list.index(track)
    if is_first:
        download_audio(
            all_ayat_list[global_index:global_index+5])
        pygame.mixer.music.load(audio_files[0])
        pygame.mixer.music.play()
        is_first = False
    else:
        pygame.mixer.music.load(audio_files[1])
        pygame.mixer.music.play()
        download_audio(
            all_ayat_list[global_index:global_index+5])
    timer.start(100)  # it contol status


def pause_audio():
    global pause_status
    pause_status = True
    print("pause")
    pygame.mixer.music.pause()


def unPaues_audio():
    global pause_status
    pause_status = False
    print("unpause")
    pygame.mixer.music.unpause()


def stopAudio():
    pygame.mixer.music.stop()
    timer.stop()


def download_audio(tracks: list):
    global audio_files
    audio_files = []
    if not os.path.exists("/tmp/Ayat_Audio"):
        os.makedirs("/tmp/Ayat_Audio")
    for t in tracks:
        trc = convert_to_file(t)
        if os.path.exists(f"/tmp/Ayat_Audio/{trc[0]}"):
            audio_files.append(f"/tmp/Ayat_Audio/{trc[0]}")
            continue
        try:
            response = requests.get(trc[1])
            response.raise_for_status()  # İndirme başarısız olursa hata fırlatır
            with open(f"/tmp/Ayat_Audio/{trc[0]}", 'wb') as dosya:
                dosya.write(response.content)
            audio_files.append(f"/tmp/Ayat_Audio/{trc[0]}")
            print("Dosya başarıyla indirildi.")
        except requests.exceptions.HTTPError as errh:
            print("HTTP Hatası:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Bağlantı Hatası:", errc)
        except requests.exceptions.Timeout as errt:
            print("Zaman Aşımı Hatası:", errt)
        except requests.exceptions.RequestException as err:
            print("Bağlantı Hatası:", err)


def convert_to_file(track):
    # * https://everyayah.com/data/Abdul_Basit_Murattal_64kbps/001002.mp3
    file = "{:03d}".format(track[1])+"{:03d}".format(track[0])+".mp3"
    url = "https://everyayah.com/data/"+imam+"/"+file
    return (imam+file, url)


def handleEndEvent():
    # print("handle")
    if not pygame.mixer.music.get_busy() and not pause_status:  # ? audio processing is finished
        ayat_color()
        if current_index < len(audio_files):
            playAudio(
                track=all_ayat_list[global_index+1])
        else:
            stopAudio()


def closeEvent(event):
    pygame.mixer.quit()
    event.accept()


def ayat_color():
    global slf
    slf.ayat_moving()


pygame.mixer.init()
db = Db_Ex_pro("Kuran.db")
imam = "Abu_Bakr_Ash-Shaatree_64kbps"
pause_status = False
global_index = 0
current_index = 0
is_first = True

timer = QTimer()
timer.timeout.connect(handleEndEvent)
audio_files = []
slf = None
# ? it gets all ayat data (ayat_no,surah_id,page)
all_ayat_list = db.get_element("Ayat", column="ayat_no,surah_id,page",
                               where="where ayat_no IS NOT ?", data=(-1,), is_special=True)
db.end_process()
del db
