list = list (input())
length = len(list)
def insertion_sort(a):
    for i in range (1,length):
        j=i-1
        temp= list[i]
        while  list[j]>temp and j>=0 :
            list[j+1]= list[j]
            j-=1
        list[j+1]= temp
insertion_sort(list)
print (list)