totalPrice = 0

for i in range(5):
    carSize=input("What car size did you rent? s/m/l ")
    carSize = carSize.lower()
    rentalDuration = float(input("How many days did you rent it for? "))
    if carSize == "s": #smol car
        print("Small car costed you", 130*rentalDuration)
        totalPrice += 130*rentalDuration
    elif carSize == "m":
        print("Medium car costed you", 165*rentalDuration)
        totalPrice += 165*rentalDuration
    elif carSize == "l":
        print("Large car costed you", 220*rentalDuration)
        totalPrice += 220*rentalDuration

print(totalPrice)