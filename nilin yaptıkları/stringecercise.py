
info=input("please write a country name, population, and life expectancy with one space: ")

country_space=info.find(" ")
country_name=info[:country_space]
print("country name is: ", country_name)

pop_space=info.rfind(" ")
population=info[country_space:pop_space]
print("your population is: ", population)

life=info[pop_space:]
print("your life expectancy is: ", life,)

zeros=population.count("0")
print("number of 0 in your population is: ",zeros)

increased_pop=(int(population))*110/100
print("increased population by 10% is: ", increased_pop)

decreased_life=(int(life))*98/100
print("life expectancy decreased by 2% is: ", decreased_life)
