import os
import pygame
import requests
from PySide6.QtCore import QTimer
from src.static.stc1 import stc as st
# TODO: when playing Ayat, it sholud download sound


def playAudio(track):
    #if track[0] == -1:
    #    track = (1, track[1], track[2])
    print(audio_files)
    print(st.crt_Ayat_i)
    global pause_status
    pause_status = False
    # ? it download 5 Ayat for the first time
    global is_first
    if is_first:
        download_audio(
            all_ayat_list[st.crt_Ayat_i:st.crt_Ayat_i+5])
        pygame.mixer.music.load(audio_files[0])
        pygame.mixer.music.play()
        is_first = False
    else:
        pygame.mixer.music.load(audio_files[1])
        pygame.mixer.music.play()
        download_audio(
            all_ayat_list[st.crt_Ayat_i:st.crt_Ayat_i+5])
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
    global is_first
    is_first = True
    timer.stop()


def download_audio(tracks: list):
    global audio_files
    audio_files = []
    if not os.path.exists(st.Ayat_f):
        os.makedirs(st.Ayat_f)
    for t in tracks:
        trc = convert_to_file(t)
        file = f"{st.Ayat_f}/{trc[0]}"
        
        if os.path.exists(file):
            audio_files.append(file)
            continue
        try:
            response = requests.get(trc[1])
            response.raise_for_status()  # İndirme başarısız olursa hata fırlatır
            with open(file, 'wb') as dosya:
                dosya.write(response.content)
            audio_files.append(file)
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
    if track[0] != -1:
        file = "{:03d}".format(track[1])+"{:03d}".format(track[0])+".mp3"
    else:
        file = "bismillah.mp3"
    url = "https://everyayah.com/data/"+imam+"/"+file
    return (imam+file, url)


def handleEndEvent():
    # print("handle")
    if not pygame.mixer.music.get_busy() and not pause_status:  # ? audio processing is finished
        st.crt_Ayat_i+=1
        ayat_color()
        playAudio(track=all_ayat_list[st.crt_Ayat_i])


def closeEvent(event):
    pygame.mixer.quit()
    event.accept()


def ayat_color():
    global slf
    slf.Ayat_coloring()


pygame.mixer.init()
imam = "Abu_Bakr_Ash-Shaatree_64kbps"
pause_status = False
is_first = True
all_ayat_list = st.all_ayat_list
timer = QTimer()
timer.timeout.connect(handleEndEvent)
audio_files = []
slf = None
# ? it gets all ayat data (ayat_no,surah_id,page)
