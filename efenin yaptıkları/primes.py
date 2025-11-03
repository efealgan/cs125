#Write a Python program that checks if a given positive integer is a prime number or not using a for
#loop. A prime number is a positive integer greater than 1 divisible only by 1 and itself
prime = True #assume true

number = int(input("provide a positive integer"))
if number == 1:
    prime = False

elif number > 0:
    for i in range(2, number):
        if number%i == 0:
            print("The number you provided (", number, ") isn't a prime number. It can be divided to:", i)
            prime = False
            break


else:
    print("You didn't provide a positive integer.")
    prime = False


if not prime:
    print("That is not a prime number.")
else:
    print(number, "is a prime number.")