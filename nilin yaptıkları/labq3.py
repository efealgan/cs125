
income=float(input("please enter annual income: "))
dependents=float(input("please enter number of dependents: "))

if income<=0 or dependents<=0: 
    print("not eligible for aid")

elif income>5000:
    aid=1000*dependents
    print("total aid for family: ", aid)

elif 5000>income>3000:
    aid=1500*dependents
    print("total aid for family: ", aid)

elif income<3000:
    aid=2000*dependents
    print("total aid for family: ", aid)
