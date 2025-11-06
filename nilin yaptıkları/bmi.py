height=float(input("pls enter your height nigga in meters: "))
weight=float(input("pls do the same with your weight in kg: "))

bmi=weight/(height**2)

print("your bmi is: ", bmi)

if bmi<25:
    print("healthy")

if bmi>25:
    print("unhealthy")

