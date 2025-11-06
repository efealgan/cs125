"""
info_input=input("enter id and name: ")
id=info_input[0:10]
name=info_input[11:]
print("name is: ", name, "id is: ", id)
start_year=int(id[0:4])
print("start year is: ", start_year)
graduation_year=start_year+5
left_years=2025-start_year
print("grad year is: ", graduation_year, "left years are: ", left_years, info_input.strip())
"""
"""
info=input("enter country, population, life expectancy with a single space: ")
country=info[0:info.find(" ")]
population=info[info.find(" "):info.rfind(" ")]
life_expectancy=info[info.rfind(" "):-1]
print(country)
print("zeros in population", info.count("0"))
increased_pop=(int(population)*110)/100
decreased_life_expectancy=(int(life_expectancy)*98)/100
print("pop increased:", increased_pop)
print("decreased life: ", decreased_life_expectancy)
"""
"""
import math
side_a=int(input("enter side a: "))
side_b=int(input("enter side b"))
side_c=int(input("enter side c: "))
perimeter=side_a+side_b+side_c
s=perimeter/2
area=math.sqrt((s)*(s-side_a)*(s-side_b)*(s-side_c))
print("area: ", float(area) )
print("perimeter: ", float(perimeter))
"""
"""
info=input("enter name, birth year, birth month with commas: ")
name=info[0:info.find(",")]
birth_year=info[info.find(",")+1:info.rfind(",")]
birth_month=info[info.rfind(",")+1: ]
age=2025-int(birth_year)
print("welcome", name, "you were born in", birth_month, "and this year you are", age)
"""
"""
integer=input("enter two digit number: ")
first=int(integer[0])
second=int(integer[1])
sum=first+second
print("sum of", first,"and",second,"is",sum)
"""
"""
import math
info=input("enter salary and bonus with one space: ")
salary=float(info[:info.find(" ")])
bonus=float(info[info.rfind(" "):])
print("your salary is: ", round(salary,2))
total_income=salary+bonus
print(f"your total income {round(total_income,2)}")
difference=abs(salary-bonus)
print("your difference is: ", difference)
"""

info=input("enter currency, calling code, country name: ")
currency=info[0:3]
calling_code=info[4:7]
country_name=info[8:]
print("country:", country_name)
print("curreny:", currency)
print("calling code:" ,calling_code)












