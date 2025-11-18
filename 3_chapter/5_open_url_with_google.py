import subprocess

url = "https://www.youtube.com/watch?v=BGJNFXgfsKY"

# открыть ссылку в Firefox
subprocess.call(['open', '-a', 'Google Chrome', url])
