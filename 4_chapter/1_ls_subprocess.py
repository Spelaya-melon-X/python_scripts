import subprocess
import sys

people_input = input("ввдеите функцию которую хотите вывести") 
command = people_input.split()  if sys.platform != 'win32' else ['dir']

try : 
    result = subprocess.run(command, capture_output=True , text = True , check=True) 
    print("Выводим команду")
    print(result.stdout) 

except subprocess.CalledProcessError as e : 
    print("Выводим ошибку")
    print(result.stderr)