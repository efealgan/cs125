oyield = 0
price = 0
bonus = False

oyield = float(input("Total yield this year (in kg): "))
price = float(input("Selling price per kilogram: "))

sale = oyield * price

if oyield > 50:
    sale += 100
    bonus = True

print("Total revenue: ", str(sale),".", sep= "")
if bonus:
    print("Claimed the high volume bonus of $100!")
