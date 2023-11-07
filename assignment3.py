card_num= input("enter the card numver : ")
last_digit= int (card_num[-1])
list_num= list (card_num)
new_list= []
for item in list_num:
    a= int (item)
    new_list.append(a)
new_list.pop(-1)
rev_list= new_list[::-1]

length= len(rev_list)
for i in range (length):
    if i%2==0:
        rev_list[i]= rev_list[i]+ rev_list[i]
        
for i in range (length):
    if rev_list[i]>=9:
        rev_list[i] = rev_list[i]-9

total= sum(rev_list,last_digit)
print (total)

if total%10==0:
    print ("the card number is valid")
else :
    print ("the card number is not valid")
