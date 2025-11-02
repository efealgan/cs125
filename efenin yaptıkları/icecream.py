chocoOrders = 0
customersTotalAge = 0

for i in range(1,6):
    selectedFlavor = input("What's your favorite flavor? [C]hocolate or [V]anilla?\n")

    if selectedFlavor.lower() == 'c':
        chocoOrders += 1

    customersTotalAge += int(input("What's your age?\n"))

print("A total of", chocoOrders, "customers preferred chocolate flavor.")
print("The average age of our customers was:", customersTotalAge/5)



