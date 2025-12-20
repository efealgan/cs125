
"""
list=[]
sum=0
year=0
this=False
for i in range(4):
    email=input("enter email pls: ")
    value=email.find("@")
    start_year=int(email[value-4:value])
    name=email[:value-4]
    total_year=2022-start_year
    if total_year>10:
        list.append(name)
        sum+=total_year
        this=True
        year+=1
if this:
    print("employees over 10 years: ", list)
    avg=float(sum/year)
    print("average employee years: ", avg)
else:
    print("no employee over 10 years")
"""




price=0
service=input("enter service (f/m/p/mc): ").lower()
if service=="m":
    question=input("vip customer y/n? ").lower()
    if question=="y":
        price=250-(250*0.15)
        print(f"your bill is {price} $")
    else:
        print("your bill is 250 $")
elif service=="f":
    question=input("vip customer y/n? ").lower()
    if question=="y":
        price=175-(175*0.15)
        print(f"your bill is {price} $")
    else:
        print("your bill is 175 $")

elif service=="p":
     print(f"your bill is 150 $")
elif service=="mc":
     print(f"your bill is 90$")
else:
    print("invalid choice")





"""
total_credit=0
total_grade=0
courses={"ENG101":3,
         "ENG102":3,
         "MATH105":3,
         "MATH106":4,
         "MBG110":3,
         "PSYC103":3,
         "TURK101":2,
         "TURK102":2,
         "CS125":3}

user_input=int(input("enter number of courses: "))
for i in range(user_input):
    code=input("enter course code: ")
    grade=float(input("enter grade point: "))
    if code in courses:
        credit=courses[code]
        total_grade+=grade*credit
        total_credit+=credit
    else:
        print(f"{code} not found")
       
gpa=float(total_grade/total_credit)
print("semester gpa: ", round(gpa,1))
"""












































