import random
numbers = []
numbersLessThanInputCount = 0

for i in range(10):
    numbers.append(random.randint(1,100))

print("Original list:",numbers)

userInput = int(input("give number"))
print("Values less than " ,userInput,":", end="", sep="")

for i in range(len(numbers)):
    if numbers[i] < userInput:
        print(numbers[i], end= " ")
        numbersLessThanInputCount += 1

print("\nPercentage of values less than ", userInput, ": ", numbersLessThanInputCount/len(numbers)*100, "%",sep="")


