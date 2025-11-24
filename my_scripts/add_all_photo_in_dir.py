import os
import shutil

def make_dir(dir) : 
    if not os.path.exists(dir):
        os.makedirs(dir)

desktop_path = os.path.expanduser("~/Desktop")
photo_dir = os.path.join(desktop_path, "photo")
pdf_dir = os.path.join(desktop_path, "pdf-ки")

people_input = int(input(" 1 - skrins \n 2 - pdfki \n Выберите действие: \n"))

dir = ""

match people_input :  
    case 1 : 
        dir = photo_dir
        make_dir(dir) 
        
        file_list = os.listdir(desktop_path)
        
        for file in file_list:
            file_path = os.path.join(desktop_path, file)
            if os.path.isfile(file_path) and "экран" in file.lower():
                shutil.move(file_path, dir)
                os.chmod(os.path.join(dir, file), 0o755)
        
    case 2 : 
        dir = pdf_dir 
        make_dir(dir) 
        
        file_list = os.listdir(desktop_path)
        
        for file in file_list : 
            file_path = os.path.join(desktop_path , file) 
            if os.path.isfile(file_path) and file.lower().endswith(".pdf"):
                shutil.move(file_path , dir)
                os.chmod(os.path.join(dir , file) , 0o755)
        
        
    case _: 
        print("Неверный ввод")
        exit()








print("Готово! Все файлы с 'экран' перемещены в папку photo.")
