population_data = {'Canada':38250000,'India':1380004385,'China':1444216107,'Turkiye': 85000000,'Russia': 
145912025,  'Japan': 126476461,  'Germany': 83783942, 'France': 65273511,   'Thailand': 71600000,  'Italy': 
6031711 } 

area_data = {'Turkiye': 783356, 'Canada': 9984670, 'China': 9596961, 'Brazil': 8515767, 'Russia': 17098242, 
'Japan': 377975, 'Germany': 357022, 'France': 551695, 'UK': 243610, 'Italy': 301340 } 


country_name=input("enter country to search: ")
if country_name in population_data.keys():
    print("Population of", country_name, "is", population_data[country_name])

else: 
    print(country_name, "not found!")



density_data = {}                                                           
for key in population_data.keys():
    if area_data.get(key, -1) != -1:
        density_data[key] = population_data[key]/area_data[key]
    else:
        print("Cannot calculate density - no area data for", key)

minDensity = int(input("Enter minimum density: "))

print("Countries with density over ", minDensity, ":", sep="")
printCounter=0
for key in density_data.keys():
    if density_data[key] > minDensity:
        print(key)
        printCounter+=1

if not printCounter:
    print("None")


