FILENAME = "file.txt"

def write() : 
    messege = input("input text pls : ") 
    with open(FILENAME , 'a') as file : 
        file.write(f"{messege} \n") 

def read() : 
    with open(FILENAME , 'r')  as file : 
        for message in file : 
            print(message , end=" ")
        print()

while(True) : 
    selection = int(input(" 1.Запись в файл\t\t2.Чтение файлa\t\t3.Выход\n Выберите действие:"))
    match selection : 
        case 1 : write( ) 
        case 2 : read( )
        case 3 : break 
        case _ : print("uncurrend input") 
    print("конец . Пока пока . ")
    

#! для того , чтобы сделать так , чтобы не возникала ошибка "invalid literal for int() with base 10: ''" необходимо try - except написать для обработки этого случая
