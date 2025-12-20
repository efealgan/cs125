

import numpy as np
cities=np.array(['Istanbul','Ankara','Izmir','Bursa','Antalya'])
first_dose=np.array([6197550, 2652085,2136705,1272038,1055350])
second_dose=np.array([2419591,1241906,1006223,550539,530415])
population=np.array([15462452,5663322,4394694,3101833,2548308])

#Calculate and display the total number of doses (first and second) for each city.
total_doses=np.array(first_dose+second_dose)
print("total dose: ", total_doses)

#total doses (first and second) for all cities.
total_doses_for_cities=np.sum(total_doses)
print("total dose for all cities: ", total_doses_for_cities)

#average number of doses for the top 5 cities.
avg_per_city=np.mean(total_doses)
print("avg is: ", avg_per_city)

#number of vaccinated citizens in each city who received only first dose.
only_first_dose=np.array(first_dose-second_dose)
print("only got the first dose: ", only_first_dose)

#percentage of those with first dose who have not received second
percentage=np.array(only_first_dose/first_dose*100)
print("percentage of only first dose: ", np.round((percentage),2))

# percentage of population in each city fully vaccinated (two doses).
percentage_fully_vaccinated=np.array(second_dose/population*100)
print("fully vaccinated: ", np.round((percentage_fully_vaccinated),2))

#names of the cities whose percentage fully vaccinated is over 20%.
is_over=np.array(percentage_fully_vaccinated>20)
is_over_cities=cities[is_over]
print("cities with over 20%: ", is_over_cities)

#maximum vaccination rate, and the name of the city and its population
max_vac_rate_index=np.argmax(percentage_fully_vaccinated)
max_vac_rate=np.round(np.max(percentage_fully_vaccinated),1)
max_vac_city=np.array(cities[max_vac_rate_index])
print(f"{max_vac_city} has the max rate of {max_vac_rate}% and a pop of {population[max_vac_rate_index]}")



