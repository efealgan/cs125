import random
numbers= [1,2,3,4,5,6,7,8,9]
number= random.choice(numbers)

guess=int(input("please pick a number bw 1-9: "))

if number==guess:
    print("well guessed!")

else:
    print("wrong guess!")
