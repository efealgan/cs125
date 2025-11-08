
name_and_id=input("please enter your id in 10 digits and your name surname: ")

id=(name_and_id[0:10])

print("your id is: ",id)

name=name_and_id[10:]
print("your name is: ", name)

start_year=int(id[0:4])
graduation_year=start_year+5

print("your graduation year is:", graduation_year)
print("you have", graduation_year-2025, "years left to graduate")
