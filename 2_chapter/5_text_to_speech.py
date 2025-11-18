import os 
from gtts import gTTS # type: ignore #  это библиотека Python, которая использует API Google для преобразования текста в речь


with open('text.txt' , 'r') as file : 
    text = file.read()

tts = gTTS(text , lang='ru')
tts.save('output_file.mp3')
os.system('afplay output_file.mp3') # mpv на линукс ( )