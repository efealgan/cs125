print("You flip a coin, and I'll deduce the result!")

print("Was it heads?")

usrinput = input()

if usrinput == "y":
    print("It is heads!")

else:
    print("Is it tails?")
    usrinput = input()
    if usrinput == "y":
        print("Then it is tails!")
    else:
        print("Then it landed on it's sides.")
