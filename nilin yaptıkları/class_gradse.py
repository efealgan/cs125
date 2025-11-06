
grade=float(input("please enter ur grade: "))

if 100<grade>0:
    print("enter between 0-100")

elif 100>=grade>90:
    print("your grade is A")
elif 90 >= grade > 80:
    print("your grade is B")
elif 80 >= grade > 70:
    print("your grade is C")
elif 70 >= grade > 60:
    print("your grade is D")
else:
    print("your grade is F")
print("done")
