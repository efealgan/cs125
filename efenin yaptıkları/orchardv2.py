oyield = float(input("Total yield this year (in kg): "))
price = float(input("Selling price per kilogram: "))

if oyield > 50:
    oyield = oyield - 50                        #remove the first 50 to reach excess amount
    aboveFiftyPrice = oyield * price * 1.5      #sell the excessive amount for a higher price
    normalPrice = 50 * price                    #find the normal price for the first 50 kgs
    totalPrice = normalPrice + aboveFiftyPrice  #add the prices

else:
    totalPrice = oyield * price

print("Sold apples for a total of:",totalPrice)
