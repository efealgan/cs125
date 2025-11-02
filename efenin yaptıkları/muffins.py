muffin_number=int(input("pls enter the muffins you baked today: "))
fullprice_muffin=int(input("enter the number of containers you sold at full price: "))*3

muffin_number_is_legal = False

while True:
    if fullprice_muffin > muffin_number:
        print("You don't have that many muffins silly :)")
        fullprice_muffin=int(input("enter the number of containers you sold at full price: "))*3
    else:
        break


print("sold muffins are: ", fullprice_muffin)

notsold_muffin=muffin_number-fullprice_muffin

discounted_containers=notsold_muffin//5

print("the discounted containers sold are: ", discounted_containers)

squirrel=notsold_muffin%5

print("the number of muffin(s) the squirrel will it is/ are: ", squirrel)

print("the total revenue is: ", (fullprice_muffin/3)*200+discounted_containers*100)

