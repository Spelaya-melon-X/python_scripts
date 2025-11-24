#  они не изменяемы 
# есть хэширование ( поэтому можно их использовать в качестве ключей в словарях )ч
#  доступ - по индексу

my = (1 , "hello" , 3.12 , "green" , 1,2,2,3,4) ; print(" просто кортеж :  "  ,  my )

sub = my[1:4] ; print(" подкортеж : " , sub)

combination = my + sub + tuple( [52] )  ; print(" объединение кортежей :  " , combination)

new_tuple = my  + (7, ) ; print( " добавление элемента в конец кортежа : " , new_tuple)

element_to_check = "green" 
if element_to_check in my : 
    print(" Элемент есть в кортеже ")
else : 
    print(" Элемента нет в кортеже ")


print("кол-во 1 в кортеже : " , my.count(1))

print( f" элемент { element_to_check} находиться на индексе :  " , my.index(element_to_check))

print( "длина кортежа : " , len(my) )

dictionary = { "a" : my , "b" : 2 , "c" : 3 }
for key in dictionary : 
    print( "%s: %s" %(key, dictionary[key]) )
    
    
