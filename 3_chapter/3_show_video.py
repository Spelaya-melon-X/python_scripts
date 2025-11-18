import moviepy
from moviepy.editor import VideoFileClip # работает под pip install moviepy==1.0.3

video_path = input("введите пожалуйста имя файла который вы бы хотели воспроизвести")
video = VideoFileClip(video_path)

video.preview()
video.close()