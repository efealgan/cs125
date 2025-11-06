
"""
#sell muffin container, 3 muffins 200 tl
#muffins left container, 5 muffins, 100 tl
#not sold muffins to squirrels

muffin_number=int(input("Enter muffin number: "))
container_number=int(input("Enter container sold at full price: "))

not_sold=muffin_number-(container_number*3)
print("muffins not sold is: ", not_sold)
discounted_bags= not_sold//5
print("discounted numbers are: ", discounted_bags)
squirrel=discounted_bags%5
print("left for squirrels are: ", squirrel)
print("total gain: ", (container_number*200)+(discounted_bags*100))

number=round(3.98685994,3)
print(number)
"""
"""
################################################################################
import math
area_of_square=float(input("enter area: "))
side_lenght=round(math.sqrt(area_of_square))
print(side_lenght)
"""
"""
###########################################################
import math
side_length= float(input("enter side lenght: "))
area=side_length**2
print("rounded up", math.ceil(area))
print("rounded down", math.floor(area))
print("rounded", round(area,2))
"""
"""
population=85919381
annual_increase=0.0067
estimated_population=int((population)/(1+annual_increase))
print("estşmated pop: ",estimated_population)


import math
area=int(input("enter area: "))
print("the abs value:", abs(area))
side=math.sqrt(area)
print("lenght: ", round(side,2))
print(side, "is bw", math.floor(side), "and", math.ceil(side))

"""
"""
# import math
# radius=int(input("enter radius: "))
# volume=(4/3*math.pi)*(radius**3)
# print("your volume is: ", volume)
"""
"""
distance=int(input("enter distance in km: "))
distance_miles=distance*0.621371
print("your km in miles is: ", distance_miles, "km")
"""
"""
income=int(input("enter monthly income: "))
rent=int(input("enter rent: "))
groceries=int(input("enter groceries: "))
insurance=int(input("enter insurance: "))
total_expenses=rent+groceries+insurance
remaining_balance=income-total_expenses
print("your total expenses are: ", total_expenses)
print("your remaining balance is: ", remaining_balance)
"""
exam_one=int(input("enter first exam score: "))
exam_two=int(input("enter second exam score: "))
exam_three=int(input("enter third exam score: "))
average=(exam_one+exam_two+exam_three)/3
print("average of exams is: ", round(average,2))














