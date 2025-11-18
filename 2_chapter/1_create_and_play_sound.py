import pyaudio  # type: ignore
import wave # wave — это стандартная библиотека Python, предназначенная для чтения и записи файлов в формате WAV.


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100 
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav" 

audio = pyaudio.PyAudio() # подключаемся к аудиокарте 

print("откытие потока для чтения данных ")
stream = audio.open(format= FORMAT , channels=CHANNELS , rate= RATE , input=True ,  frames_per_buffer=CHUNK) # создаем поток для чтения данных с устройства записи 

print("начало записи ")


frames = []
for _ in range( 0 , int(RATE / CHUNK * RECORD_SECONDS)) : 
    data = stream.read(CHUNK)
    frames.append(data)
    
print("запись завершнена")

stream.stop_stream()
stream.close()

audio.terminate()

with wave.open(WAVE_OUTPUT_FILENAME , "wb") as wf :  # wb - write binary записываем в бинарном формате
    wf.setnchannels(CHANNELS) # установить кол-во каналов 
    wf.setsampwidth(audio.get_sample_size(FORMAT)) 
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames)) # тут мы записали в бинарном формате данные , которые записывали с устройства записи


def play_sound(filename) : 
    wf = wave.open(filename , "rb")  # rb - read binary чтение в бинарном формате
    p = pyaudio.PyAudio()
    
    
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()) , channels=wf.getnchannels() , rate=wf.getframerate() , output=True) 
    #get_format_from_width -  преобразует ширину выборки (размер сэмпла в байтах) в числовой формат
    data = wf.readframes(CHUNK)
    while data : 
        stream.write(data)
        data = wf.readframes(CHUNK)
    
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
play_sound(WAVE_OUTPUT_FILENAME)
    