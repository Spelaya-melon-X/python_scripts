import subprocess 
cmd = "cat file.txt"
subprocess.call(cmd , shell=True)

print("\n")

filepath = "file.txt"
with open(filepath , 'r') as file:  # для чтения из файла ("r" - read)
    data = file.read()
    print(data)
    
print("\n еще один способ ")

with open(filepath , 'r' , encoding="utf-8") as file : 
    text = file.read() 
    print(text)


print("\n")

with open(filepath , 'w') as file :  # для добавления в файл ('a' - append )
    text = "HIHI HAHA" 
    file.write( text )
print("текст добавлен !) \n")


# запись в файл список 
lines = ["1 word \n" , "2 word\n" , "4 word \n"]  # линия , а также перевод - строчка 
with open(filepath , 'a') as file : 
    file.writelines(lines)  



# чтение 9 знаков из файла 
with open(filepath , 'r' , encoding="utf-8" ) as f: data = f.read(8) 
print(data)


