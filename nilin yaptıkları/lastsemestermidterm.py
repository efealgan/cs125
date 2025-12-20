
"""
import random
list=[]
total_element=0
for i in range(10):
    numbers=random.randint(1,100)
    list.append(numbers)
print(f"original list: {list}")
value=int(input("enter value: "))

for numbers in list:
    if numbers<value:
        total_element+=1
percentage=int((total_element/10)*100)
print(f"percentage of elements less than {value}: {percentage} %")
list.sort()
print(f"sorted list: {list}")
"""
"""
happiness=('Hungary', 27.57,51,'Brazil',25.04,49,'Australia',23.83,12,'Romania',21.09,24,'Czechia',21.01,18,'Canada',20.37,13)
countries=happiness[0::3]
pet_ownership=happiness[1::3]
happiness_rank=happiness[2::3]
print(countries)
print(pet_ownership)

most_pet=pet_ownership[0]
country=countries[0]
sum=0
total=0

for pet in pet_ownership:
    sum+=pet
    total+=1
    if pet>most_pet:
        most_pet=pet
        index=pet_ownership.index(pet)
        country=countries[index]
    avg=int(sum/total)

print(f"{most_pet} % of people in {country} own pets")
print(f"average pet ownership: {avg} %")

"""





ankara={"Louise":3,
        "Trilye": 4,
        "Pizzeria Alla Torre": 5,
        "Timboo": 2,
        "Loca": 1,
        "Fige": 5}

print("1. Search Restaurant by name",
      "\n2. Search Restaurant by stars",
      "\n3. Add new restaurant",
      "\n4. Delete restaurant",
      "\n5. Display all restaureant")
choice=input("enter choice (1-5): ")

if choice=="1":
    restaurant_name=input("enter retaurant name: ")
    if restaurant_name in ankara:
        print(restaurant_name)
        print(restaurant_name,ankara[restaurant_name]*"*")
    else:
        print(f"{restaurant_name} not found")
elif choice=="2":
    stars=int(input("enter stars: "))
    print("restaurant wşth or more",stars,":")
    for star in ankara:
        if stars<=ankara[star]:
            print(star)
elif choice=="3":
    new=input("enter new restaurant name: ")
    new_star=int(input(f"enter number of stars {new}:"))
    ankara[new]=new_star
    print(f"{new} added")
elif choice=="4":
    name=input("enter restaurant: ")
    if name in ankara:
        ankara.pop(name)
        print(f"{name} deleted")
    else:
        print("restaurant not found")
elif choice=="5":
    for restaurants in ankara:
        print(restaurants,ankara[restaurants]*"*")
else:
    print("invalid input!")

















































