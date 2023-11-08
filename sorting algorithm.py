list= list(input())
length = len(list)
#bubble sort
def bubble_sort (a=[]):
    for i in range (length):
        for j in range (i+1,length):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
bubble_sort(list)
print ("bubble sorted list  {}".format(list))
new_list = []
#selection sort
def selection_sort(b=[]):
    for i in range (0,length):
        min_value = min(list)
        new_list.append(min_value)
        list.remove(min_value)
selection_sort(new_list)


print ("selection sorted list {}".format(new_list))