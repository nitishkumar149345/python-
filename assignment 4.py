f1= open("assign_text","r")
data= f1.read()

dic = {}
new_dic= {}
for x in range (97,123):
    a= chr(x)
    count =0
    for i in data:
        if i==a:
            count+=1
            dic[a]=count
print (dic)
word_count=0
for i in data:
    if i==" ":
        word_count +=1
print ("total words in file= {}".format(word_count))

for x in range (97,123):
    a= chr(x)
    count =0
    for i in data:
        if i==a:
            count+=1
            ratio= count/word_count
            new_dic[a]= "%.2f"% ratio
print (new_dic)