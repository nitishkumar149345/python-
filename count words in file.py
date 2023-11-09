
f1= open("file_1.txt","r")
data= f1.read()
count= 0
for i in data:
    if i == " ":
        count +=1
print (count+1)