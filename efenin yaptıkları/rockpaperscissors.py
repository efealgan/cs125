import random
while(True):
    moves = {"R":0, "P":1, "S":2}
    playerMove = moves[input("R/P/S: ").capitalize()]
    computerMove = random.randint(0,2)
    if playerMove == 0: #Rock
        if computerMove == 1: #Paper
            print("You Lose")
        elif computerMove == 2: #Scissors
            print("You Win")
        else:
            print("It's a tie!")
    #Paper
    #Scissors
    response = input("Do you want to keep playing? ")
    if response.capitalize() != "Y":
        break

print("Thanks for playing")