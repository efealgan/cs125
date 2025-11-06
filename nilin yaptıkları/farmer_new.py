
apple_yield=int(input("please enter the total yield of apples in kg: "))
selling_price=int(input("please enter the selling price per kg: "))

if apple_yield>50:
    earning=selling_price*50+ (apple_yield-50)*selling_price*1.5
   
else:
     apple_yield<=50
     earning=selling_price*apple_yield
print("your earning is: ", earning, "$")      