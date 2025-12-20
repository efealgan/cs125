"""
list=
list=[]
mean=0
for i in range(1,13):
    month=float(input(f"enter mean temp of month {i}: "))
    mean+=month
    list.append(month)
average=mean/12
print(f"months temp above {average}: ")
for i in range(12):
    if i>average:
        temperature=list[i]
        print(f"month {i} has a temp of {temperature}")
"""
"""
total=0
list=('CS 125',3),('HIST 200',4),('PHIL 243',6),('POLS 304',3), ('ENG 101',3)
print("first year courses: ")
for tuples in list:
    course=tuples[0]
    course_year=course[-3]
    credit=tuples[1]
    if course_year=="1":
        print(course)
        total+=credit
print(f"total credits for first year: {total}")
"""

dic={"honda":125000,
     "passat": 135000,
     "yaris":55000,
     "toureg":255000,
     "civic":95000}
print(dic)

for key in dic:
    if dic[key]>100000:
        print("price over 100k: ",dic[key])
dic.pop("yaris")        
print(dic)

















