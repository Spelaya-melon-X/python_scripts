import sounddevice as sd  # type: ignore
import numpy as np # type: ignore
from scipy.io.wavfile import write # type: ignore


print(sd.query_devices()) # все дивайсы , которые есть для записи 

duration = 1 * 10 
sample_rate = 44100
print("начинают запись , говори пж пж")


audio_data = sd.rec(int(duration *sample_rate ) ,samplerate=sample_rate , channels = 1 , dtype ='int16' )  # запускаем запись звука с указанной частотой и кол-вом каналов 
sd.wait() # ожидание завершения записи 

print("запись завершена")
write('output_sounddevice_file.wav' , sample_rate , audio_data) # сохранение данных в wav формате 
print("аудио сохранено в файл output_sounddevice_file.wav")


