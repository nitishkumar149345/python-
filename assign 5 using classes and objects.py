import json

class Employees:
    def __init__(self,id,f_name,m_name,l_name,name="null",email="null"):
        self.id=id
        self.first_name= f_name
        self.middle_name= m_name
        self. last_name= l_name
        self.name = name
        self. email= email
def genereate_emails(f,m,l):
   
    a="-"
    b="."
    c="@omiwyse"
    if m=="None":
        em= (f+b+l+c).lower()
    else:
        em= (f+a+m+b+l+c).lower()
    return em
def dictionery(a={}):
    dic= {}
    for i in a:
        employee= Employees(i['id'],i['firstName'],i['middleName'],i['lastName'])
        email= genereate_emails(f=str(employee.first_name),m=str(employee.middle_name),l=str(employee.last_name))
      
        middle_name= str(employee.middle_name)
        if middle_name=="None":
            name= employee.first_name+ employee.last_name
        else:
            name= employee.first_name+employee.middle_name+employee.last_name
        employee = Employees(i['id'],i['firstName'],i['middleName'],i['lastName'],name,email)
        dic[email]= {"id":employee.id,"name":employee.name}
    return dic

f1= open("employees.json","r")
data= f1.read()
employees_details= json.loads(data)
new_dict= dictionery(employees_details['employees'])
f2= open("final_details.json","w")
final_details= json.dumps(new_dict)
f2.write(final_details)
