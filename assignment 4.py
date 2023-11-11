f1= open ("assign_text","r")
data= f1.read()
f1= open("assign_text",'w')
f1.write(data.lower())
f1= open("assign_text","r")
data= f1.read()

words= data.split()

def count_words(s= str()):
    count =0
    for i in data:
        if i== " ":
            count +=1
    return count+1

num_words= count_words(data)
print ("number of words preseent in the file : {}".format(num_words))
dic= {}
for i in words:
    frequency= 0
    for j in words:
            if j==i:
                frequency+=1
    
    dic[i]= frequency
print (dic)
dic_ratio={}
for i in words:
    frequency= 0
    for j in words:
            if j==i:
                frequency+=1
    ratio= frequency/num_words
    dic_ratio[i]= "%.2f" %ratio

print ("ratio of each word in the file")
print (dic_ratio)
