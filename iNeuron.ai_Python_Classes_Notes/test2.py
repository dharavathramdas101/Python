class Person :

    def __init__(sudh,name,surname , emailid , year_of_birth):
        sudh.name1 = name
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def __init__(sudh,name,surname ):
        sudh.name1 = name
        sudh.surname = surname

    def age(sudh , curretn_year):
        return curretn_year - sudh.year_of_birth

anuj_var  = Person("anuj" , "bhandari" , "anuj@gmail.com" , 1994)
sudh = Person("sudhanshu " ,"kumar" , "sudhanshu@gmail.com" , 23424)
gargi = Person("gargi" , "xyz" , "gargi@gmail.com" , 234242)
print(anuj_var.age(2022))

s = "sudh"
s.upper()