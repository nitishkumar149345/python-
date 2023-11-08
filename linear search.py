list= input()
key= input()
for i in range (len(list)):
    if list[i]==key:
        print ("element found at {}".format(i))
        break
    elif i==(len(list))-1:
        print ("element not found")