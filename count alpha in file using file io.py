f1= open("file_1.txt","r+")
data= f1.read()

for i in range (97,123):
    count=int (0)
    a=chr(i)

    for x in data:
        if x==a:
            count +=1
    print ("{} : {}".format(a,count))