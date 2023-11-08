list= list(input())
size= len(list)
key= input()
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