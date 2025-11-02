userInput = input("Enter a sentence: ") #take a sentence from user
hiddenMessage = ""                      #create a variable to hold our hidden message (if any)
for i in userInput:
    if i.isupper():
        hiddenMessage += i

if hiddenMessage == "":
    print("No hidden message.")

else:
    print("Your hidden message is:",hiddenMessage)



#keep Going, leaRn tO Win