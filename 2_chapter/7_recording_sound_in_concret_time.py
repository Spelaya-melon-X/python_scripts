import time
import os 
from datetime import datetime 

audio_file = "output_file.mp3"

def play_audio() : 
    os.system("afplay " + audio_file)
    

while (True) : 
    current_time = datetime.now().strftime('%H:%M')
    if (current_time == '02:12') : 
        print("пошел музон")
        play_audio()
        
        time.sleep(3) 
        print("аудиофайл остановлен")
        break
    time.sleep(1)
    