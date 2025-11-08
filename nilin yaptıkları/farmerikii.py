
apple_yield=float(input("please enter the apple yield in kg: "))
selling_price=float(input("please enter seling price of one kg: "))
earning=apple_yield*selling_price

if apple_yield>50:
    earning=(apple_yield-50)*1.5*selling_price+(50*selling_price)
    print("your earning is: ", earning, "$")

else:
    earning=apple_yield*selling_price
    print("your earning is: ",earning,"$")

