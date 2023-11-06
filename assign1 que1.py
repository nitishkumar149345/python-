a= str (input("enter string"))
l= int (len(a))
if l>10:
    b=str (a[0])
    c=str (l-2)
    d=str (a[l-1])
    e=str (b+c+d)
    print (e)
else:
    print (a)
