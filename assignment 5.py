import json
f1= open("employees.json","r")
json_dic= f1.read()

employees_details= json.loads(json_dic)

def employees_email(f_name= str(),m_name=str(),l_name=str()):
    a= "-"
    b= "."
    c= " @Omniwyse"
    if m_name=="None":
        em=f_name + l_name+b +c
    else:
        em= f_name + a + m_name + b+ l_name+c
    
    return em

dic= {}
for i in employees_details['employees']:
    first_name=  (i['firstName'])
    middel_name= str(i['middleName'])
    last_name= i['lastName']
    id= i['id']
    if middel_name=="None":
        full_name= first_name + last_name
    else:
        full_name= first_name+ middel_name+ last_name
    email= employees_email(first_name, middel_name,last_name)
    dic[email]= {"id": id, "full name": full_name}


print (dic)

