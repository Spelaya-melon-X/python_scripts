
import pyaudio # type: ignore 
import wave 
import subprocess

def record_audio(file_name , time = 5) : 
    chunk = 1024 
    sample_format = pyaudio.paInt16
    channels = 1 
    fs = 44100 
    p = pyaudio.PyAudio()
    stream = p.open(format = sample_format , channels = channels , rate = fs , frames_per_buffer = chunk , input = True)
    print("начало записи...")
    frames = []
    for _ in range(0 , int(fs / chunk * time))  : 
        data = stream.read(chunk)
        frames.append(data)
        
    print("запись завершена")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(file_name , 'wb') 
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    # конвертируем в mp3 используя ffmpeg
    subprocess.run(['ffmpeg' ,  '-y' , '-i' , file_name , file_name.split('.')[0] + '.mp3'])

if __name__ == "__main__" : 
    # file_name = "out25.mp3"
    file_name = "out25.mav"
    record_audio(file_name)

