
apple_yield=float(input("please enter the apple yield in kg: "))
selling_price=float(input("please enter the price you sell one kg: "))
earning=apple_yield*selling_price

if apple_yield>50:
    earning=earning+100
    print("your total earning is: ",earning,"$")

else:
    print("your total earning is: ",earning,"$")
