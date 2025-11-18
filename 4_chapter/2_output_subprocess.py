import subprocess

command = ['grep' , 'hello']
process = subprocess.Popen(command ,
                           stdin=subprocess.PIPE ,
                           stdout=subprocess.PIPE , 
                           text= True)

output ,error = process.communicate(input="hello world \n hello university \n piska piska piska \n hello + wibe") 
print("Output:\n" , output) 



# ---------------------- еще один пример ----------------------


command = ['grep', 'hello']
process = subprocess.Popen(command, 
                          stdin=subprocess.PIPE, 
                          stdout=subprocess.PIPE, 
                          text=True)


process.stdin.write("hello world\n")
process.stdin.write("hello university\n") 
process.stdin.write("piska piska piska\n")
process.stdin.write("hello + wibe\n")
process.stdin.close()  # Важно закрыть!

output = process.stdout.read()
print("Output:\n", output)


