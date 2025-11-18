import pyaudio  # type: ignore

FORMAT = pyaudio.paInt16  # глубина звука = 16 бит = 2 байта
CHANNELS = 1  # моно
RATE = 48000  # частота дискретизации - кол-во фреймов в секунду
CHUNK = 4000  # кол-во фреймов за один "запрос" к микрофону - тк читаем по кусочкам
RECORD_SECONDS = 5  # длительность записи

audio = pyaudio.PyAudio()

in_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK) # открываем поток для чтения данных с устройства записи по-умолчанию и задаем параметры

out_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True) # открываем поток для записи на устройство вывода - динамик - с такими же параметрами
print("recording...")

audio_recording = b''  # пустая строка из байт

# для каждого "запроса"
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  # RATE / CHUNK - кол-во запросов в секунду
    audio_recording += in_stream.read(CHUNK)  # читаем строку из байт длиной CHUNK * FORMAT = 4000*2 байт

print("finished recording")
print("now playing...")

# отправляем все что записали на колонки
out_stream.write(audio_recording)  # отправляем на динамик

# отключаемся от микрофона и динамика
out_stream.stop_stream()
out_stream.close()
in_stream.stop_stream()
in_stream.close()

# отключаемся от аудиокарты
audio.terminate()