import os 
import subprocess
# удаление файла из директории 
del_file = "temp_dir/file_del.txt"
if os.path.exists(del_file) :
    os.remove(del_file) 
else : 
    print("данного файла не существует ")

