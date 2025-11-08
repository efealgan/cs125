
#earning of the apple orchard
apple_yields=int(input("enter the total yield of apples in kg: "))
selling_price=int(input("please enter the selling price of apples of one kg: "))
earning=apple_yields*selling_price


if apple_yields>50:
    earning+=100
    print("the total earning is: ", earning, "$")
    

else:
    print("the total earning is: ", earning, "$")




