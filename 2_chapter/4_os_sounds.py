import os 
import subprocess

os.system("afplay output.wav") 


# # запись звукового файла используя ffmpeg 
# also - штука под linux , поэтому ее на mac нет 
cmd_recodring_soucnd = "ffmpeg -f avfoundation -i ':0' -ss 00:00:00 -to 00:00:15 test1.wav"
subprocess.call(cmd_recodring_soucnd, shell=True)

# штука для того , чтобы вывести список всех девайсов которые существуют ( камера + микрофон )
cmd_print_all_devices = 'ffmpeg -f avfoundation -list_devices true -i ""'
subprocess.call(cmd_print_all_devices ,shell = True) 

# скрипт для преобразования текста в речь 
# cmd_espeak_sound = "espeak -ng -s  150 -vru -f test.txt" # под линуксом 
cmd_espeak_sound = 'say -v Jester -r 150 -f text.txt' 
#? -r - скорость речи 
#? -f - название файла
#? -v - голос персонажа 
subprocess.call(cmd_espeak_sound , shell=True)



