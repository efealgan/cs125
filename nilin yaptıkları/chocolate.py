
chocolate=0
age=0
age_total=0

for i in range(1,6):
    flavour=input("enter ice cream flavour (C or V): ")
    age=int(input("please enter age: "))

    if flavour.lower() == "c":
        chocolate+=1
        
    age_total+=age
average=age_total/5

print("number of choco is: ", chocolate, "and the average is: ", average)



