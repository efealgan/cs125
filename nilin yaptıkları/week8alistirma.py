
"""
list=[]
mean=0
for i in range(1,13):
    temp_mean=float(input(f"enter temperature month {i}: "))
    mean+=temp_mean
    list.append(temp_mean)
avg=mean/12
print("average temp is: ", avg)
print(f"months with higher temp from {avg}")
for i in range(12):
    temperature=list[i]
    if temperature>avg:
        print(f"month {i+1} has temp of: {temperature}")
"""
"""
courses_credits=[('CS 125',3),('HIST 200',4),('PHIL 243',6),('POLS 304',3), ('ENG 101',3)]
print("first year courses: ")
credit=0
for i in courses_credits:
    course_name=i[0]
    if course_name[-3]=="1":
        credit+=i[1]
        print(course_name)
print("total credits: ", credit)

"""
"""
dictionary={"Honda CR-V": 125000,"Volkswagen Passat": 135000, "Toyota Yaris": 55000, "VOlkswagen Toureg": 255000, "Honda Civic": 95000}
print(dictionary)
print("prices over 10000: ")
for key in dictionary:
    if dictionary[key]>100000:
        print(key,dictionary[key])
dictionary.pop("Toyota Yaris")
print(dictionary)
"""







































