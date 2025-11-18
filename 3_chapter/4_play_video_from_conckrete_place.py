import schedule
import time 
import subprocess
import datetime 

video_path = "27.mp4"

def play_video() : 
    print(f"{datetime.datetime.now()} : Запуск видео ")
    subprocess.Popen(['open' , video_path])

schedule.every().day.at("01:12").do(play_video)
print("скрипт запущен ожидайте времени запуска скрипта")

while True : 
    schedule.run_pending()
    time.sleep(1)
    