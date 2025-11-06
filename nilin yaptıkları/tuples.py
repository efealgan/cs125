"""
gseven=("Canada", "France", "Germany", "Italy", "Japan", "UK", "USA")
quality=('Luxembourg', 'Netherlands' , 'Denmark', 'Oman', 'Switzerland','Finland' , 'Norway', 'Iceland', 'Austria', 'Germany' ,'Sweden')

common=()
for i in gseven:
    if i in quality:
        common+=(i,)
print(common)

all=gseven
for i in quality:
    if i not in gseven:
        all+=(i,)
print("updated: ",all)
"""
"""
phone={"Nil": 1, "Efe": 2}
phone["Nil"]=5
print(phone)
phone["Mahmut"]=7
phone.pop("Nil")
print(phone)

print(phone.keys())
print(phone.values())

if "Nil" not in phone:
    print("yay")

print(phone["Efe"])
print(phone.get("Efe", "gululul"))
phone["ugugugg"]=9
print(phone)
phone.pop("Mahmut")
print(phone)
for i in phone:
    print(i, phone[i])
"""

"""
car_dic={'Toyota':'Japan','Volkswagen':'Germany','Honda':'Japan','BMW':'Germany','Volvo':'Sweden'}

brand=input("Enter a brand: ")
country=car_dic[brand]
print(brand, "is from", country)

new_country=input("enter country: ")
print("cars from ", new_country)
for key in car_dic:
    if car_dic[key]== new_country:
        print(key)

"""

import math
country_data=('Hungary',27.57,51,'Brazil',25.04,49,'Australia',23.83,12,'Romania',21.09,24,'Czechia',21.01,18,'Canada',20.37,13) 
countries=country_data[0:18:3]
happiness=country_data[2:18:3]
pet_ownership=country_data[1:17:3]
print("countries: ", countries)
print("happiness: ", happiness)
print("pet pwnership :", pet_ownership)
happy=happiness[0]
sum=0
for i in happiness:
    if i<happy:
        happy=i
        index=happiness.index(i)
        country=countries[index]
        pet=math.ceil(pet_ownership[index])
    sum+=i

print("people in", country, "have the rank: ",happy)
print("average happiness: ", math.ceil(sum/len(happiness)))
print(pet, "%"," of people in ", country, " own pets", sep="")

#############################################################################################################
population_data = {'Canada':38250000,'India':1380004385,'China':1444216107,'Turkiye': 85000000,'Russia': 
145912025,  'Japan': 126476461,  'Germany': 83783942, 'France': 65273511,   'Thailand': 71600000,  'Italy': 
6031711 } 

area_data = { 'Turkiye': 783356, 'Canada': 9984670, 'China': 9596961, 'Brazil': 8515767, 'Russia': 17098242, 
'Japan': 377975, 'Germany': 357022, 'France': 551695, 'UK': 243610, 'Italy': 301340 } 


country_name=input("enter country to search: ")
if country_name in population_data.keys():
    print("the population of", country_name, "is:",population_data[country_name] )
else:
    print(country_name, "not found!")

density_data={}
for country_name in population_data:
    if country_name in population_data and country_name in area_data:
        density_country=population_data[country_name]/area_data[country_name]
        density_data[country_name]=density_country
    elif country_name in population_data and country_name not in area_data:
        print("no area data for: ",country_name)

min_density=int(input("enter min density: "))
print("countries with density over ", min_density)
for country_name in density_data:
    if density_data[country_name]>min_density:
        print(country_name)































