file = open("file_1.txt","r")
data= file.read()
c_file= open("copy_file.txt","w")
for i in data:
    c_file.write(i)
