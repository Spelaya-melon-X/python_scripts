import requests
import subprocess
url = "https://stepik.org/course/181477/syllabus"
response = requests.get(url)

if response.status_code == 200 : 
    print("Сайт доступен")
    print(response.text)
else : 
    print(f"Сайт недоступен , код ошибки {response.status_code}")
    