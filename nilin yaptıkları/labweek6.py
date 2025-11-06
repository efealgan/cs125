

list_one=["Ayşe", "Oliver", "Mehmet", "Emily","Elif"]
list_birth_year=[2002,2001,2005,2015,1999]

name=input("please enter a name: ")

for i in (len(list_one)):
    name_place=list_one.index(i)

    if name in list_one:
        list_one.remove(name)
        list_birth_year.remove(name_place)
        birth_year=list_birth_year[name_place]
        a=list_one[name_place]

    else:
     print("not found in the list")   

print(a, "was born in", birth_year )
      

























