import yt_dlp # type: ignore  , ffmpeg 
import time


def download_video_with_audio(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Лучшее видео + лучший аудио
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',  # Объединяем в mp4
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Введите ссылку на видео: ")
    
    start_time = time.time()
    download_video_with_audio(video_url)
    elapsed_time = time.time() - start_time
    
    print(f"Загрузка завершена за {elapsed_time:.2f} секунд")


