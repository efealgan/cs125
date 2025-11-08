#Input the number of muffins baked by the bakery.

total_muffins=int(input("Muffins baked today: "))

fullprice_container=int(input("Number of containers sold at full price: "))

fullprice_muffin=fullprice_container*3

print("number of muffins sold at full price: ", fullprice_muffin)

notsold_muffin= total_muffins-fullprice_muffin

print("number of muffins not sold at full price: ", notsold_muffin)

bags=notsold_muffin//5

print("number of bags sold to the charity: ", bags)

squirrel= notsold_muffin%5

print("squirrel will have: ", squirrel, "muffin(s)")

print("the total revenue of today is: ", fullprice_container*200+bags*100)

print("blyat")


