m= int (input("enter the size of employees"))
employees = []
subele= []
for i in range (0,m):
    subele= (input(),int(input()),float(input()))
    employees.append(subele)

#print (employees)
sum=0
for i in range (0,m):
    sum=sum+employees[i][2]
avg= sum/m
#print ("average hourly wage", avg)

for i in range (0,m):
    payment = employees[i][1]*employees[i][2]
    print ("{} has to be paid ${} for this week".format(employees[i][0],payment))
for i in range (0,m):
    payment = employees[i][1]*employees[i][2]
    if employees[i][2]>avg:
        print ("{} earns more than average".format(employees[i][0]))
    else :
        print("{} is earining less than average".format(employees[0][1]))


