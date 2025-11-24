from random import randrange

s = 0.1 + 0.7 
print( f"{s:.4f}") # 0.8000 

s = "aba52aba" 
digits_1 = []
for symb in s: 
    if '1234567890'.find(symb) != -1: 
        digits_1.append(symb)
print( digits_1 ) 


digits_2 = []
for symb in s : 
    if symb >= '0' and symb <= '9': 
        digits_2.append(symb)
print(digits_2)

n = 10 
a = [randrange(1,10) for i in range(n)]  ; print(a)


print(hex(n))



def mysum( *numbers) :  # при передачи 
    output = 0 
    for num in numbers : 
        output += num 
    return output 

print( mysum(1,2,3,4,5) )

def create_tuple( *args) : 
    print(args) # тут уже tuple 
    
create_tuple(1,2,3,4,5)
    
def create_dict(**kwargs) : 
    print(kwargs)
    
create_dict(a=1,b=2,c=3)
