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



size= len(list)
key= input()
def binary_search(key,list):
    l=0
    r=size-1
    while  l<r:
        mid=int ( (l+r)/2)
        if key==list[mid]:
            print ("element found at {}".format(mid))
            break
        elif key > list[mid]:
            l=mid+1
        elif key< list[mid]:
            r= mid-1
        if l==r:
            print ("element not found")

binary_search(key,list)