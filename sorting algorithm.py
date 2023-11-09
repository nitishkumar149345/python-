sort_list= list(input())
length = len(sort_list)
#bubble sort
def bubble_sort (a=[]):
    for i in range (length):
        for j in range (i+1,length):
            if a[i]>a[j]:
                a[i],a[j]=at[j],a[i]
bubble_sort(sort_list)
print ("bubble sorted list  {}".format(list))
new_list = []
#selection sort
def selection_sort(b=[]):
    for i in range (0,length):
        min_value = min(b)
        new_list.append(min_value)
        b.remove(min_value)
selection_sort(sort_list)


print ("selection sorted list {}".format(new_list))
