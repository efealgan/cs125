#q1
"""
count=0
list=[]
for i in range(280,3501):
    if i%7==0 and i%4==0:
        count+=1
        print(i,end=" ")
print("number of counts are: ",count)
"""

#q2
"""
count=0
print("numbers are: ")
for i in range(545,4751):
    if i%3==0 and i%8==0:
        count+=1
        print(i,end=" ")
print("count is: ", count)
"""
#q3
"""
sum=0
number_count=0
for iteration in range(6):
    number=int(input("enter number: "))
    if number>=0:
        sum+=number
        number_count+=1
    else:
        break

avg=sum/number_count
print("average is: ", avg)
"""


#q4
"""
sum=0
count=0
for i in range(10):
    number=int(input("enter number: "))
    if number==-9999:
        break
    else:
        sum+=number
        count+=1
avg=sum/count
print("average is: ", avg)
"""

#q5
"""
import random
list=[]
for i in range(10):
    number=random.randint(1,20)
    list.append(number)
list.sort()
print(f"the list is: {list}")

for i in list:
    list_count=list.count(i)
    print(f"the number {i} appears {list_count} times.")
"""
#q6
"""
import random
list=[]
for i in range(15):
    number=random.randint(10,40)
    list.append(number)
list.sort()
print(f"the list is: {list}")
for i in list:
    list_count=list.count(i)
    print(f"the number {i} appears {list_count} times")
"""



#q7   

digits="1234567890"
list=[]
number=input("enter number (e.g. [1, 2, 3]): ")
print(f"the type of input is: {type(number)}")
for i in number:
    if i.isdigit():
        list.append(i)
print("list is: ", list)
print(f"type of list is: {type(list)}")







#q9
"""
dic={168:("George",5000,0.10),
     179:("Eileen",8500,0.15),
     192:("James",6000,0.10),
     185:("Julia",7500,0.20),
     169:("Kim",6000,0.10)}
print(f"dictionary is: ")
print(dic)

for salary in dic:
    salary=+dic[salary][1]+(dic[salary][1]*dic[salary][2])
    for i in dic:
        name=dic[i][0]
    print(f"total salary of {name} is: {salary}")
"""
#q10
"""
sum=0
dic={"pencil":(2.40,0.05),
     "eraser": (4.50,0.10),
     "sharpener":(7.80,0.20),
     "crayon":(3.00,0.10),
     "notebook": (8.60,0.25)}
print(dic)
for i in range(3):
    name=input("enter name: ")
    if name in dic:
        price=dic[name][0]-(dic[name][0]*dic[name][1])
        sum+=price
print(f"total price is: {sum}")
"""

#q11
"""
for i in range(5):
    name=input("enter name: ")
    if name.lower()!="stop" and name.lower()!="quit":
        title=input("enter title: ")
        last_space=name.rfind(" ")
        surname=name[last_space:]
        actual_name=name[:last_space]
        print(f"official name is: {surname}, {title} {actual_name}")
    else:
        break
print("Program Complete...")
"""

#q12
"""
for i in range(1,5):
    name=input("enter name :")
    title=input("enter title: ")
    last_space=name.rfind(" ")
    surname=name[last_space:]
    actual_name=name[:last_space]
    print(f"official name: {surname}, {title} {actual_name}")
"""
#q13
"""
for i in range(1,51):
    if i%5==0 and i%3==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
"""   
#q14
"""
for i in range(136,251):
    if i%4==0 and i%7==0:
        print("boomloom")
    elif i%4==0:
        print("boom")
    elif i%7==0:
        print("loom")
"""

#q15
"""
sum=0
string=input("enter a string: ")
for i in string:
    if i.isdigit():
        sum+=int(i)
print("sum of the digits are: ",sum)
"""
"""
#q16
count=0
string=input("enter a string: ")
for i in string:
    if i.isdigit():
        count+=1
print("number of digist: ", count)

"""



































