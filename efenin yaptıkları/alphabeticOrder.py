#Write a Python program that takes a string as input and checks if the characters in the string are in alphabetical order using a for loop. 
#Ignore any non-alphabetic characters
# a < b < c | true
alphabet = "abcdefghijklmnopqrstuvwxyz"
inputString = input("say something ")
inputString = inputString.lower()
yippi = True
for i in range(len(inputString)-1):
    letter = inputString[i]

    if not letter in alphabet:
        print("Encountered non-alphabetical character: \"", letter,"\" skipping.", sep="")
        continue

    elif  letter > inputString[i+1]: # is NOT in alphabetical order
        print(letter, "and", inputString[i+1],"are not in alphabetical order.")
        yippi = False 
        break


if yippi:
    print("your sentence was in alphabetical order!!!!")