import random
secret = random.randint(1,20)
correct = False
for i in range(1,6):
    guess = int(input("guess: "))
    if guess == secret:
        print("you got it right in", i, "tries!")
        correct = True 
        break
    elif guess>secret:
        print("try lower")
    else:
        print("try higher")

if not correct:
    print("better luck next time")