#Input the number of muffins baked by the bakery

muffin_number=int(input("enter muffins baked today: "))

#Input the number of containers sold at full price by the bakery

muffins_sold_fullprice=int(input("enter number of containers sold at full price: "))*3
print("muffins sold at full price are:", muffins_sold_fullprice)

#Calculate and display the number of muffins not sold.

muffins_notsold=muffin_number-muffins_sold_fullprice
print("muffins not sold at full price are: ", muffins_notsold)

#Calculate and display the number of bags made and sold at the discounted price

discountedbags=muffins_notsold//5
print("packages sold for lower price are: ", discountedbags)

#Calculate and display the number of muffins left out for the squirrels

squirrel=muffins_sold_fullprice%5
print("the muffin(s) the squirrel had: ", squirrel)

#Calculate and display the money earned by the bakery.

print("the money earned is: ", ((muffins_sold_fullprice/3)*200)+(discountedbags*100))


