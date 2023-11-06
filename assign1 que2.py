m= int (input("enter marks:"))
if m<0 or m>100:
    print ("invalid marks")
elif m>=95:
    print ("grade= A+")
elif  m>90:
    print ("grade= A")
elif m>=85 :
    print ("grade= B+")
elif m>=80:
    print ("grade= B")
elif m>=75:
    print ("grade= C+")
elif m>=65:
    print ("grade= C")
elif m>=55:
    print ("grade= D+")
elif m>=45:
    print ("grade= D")
elif m<45:
    print("fail")
