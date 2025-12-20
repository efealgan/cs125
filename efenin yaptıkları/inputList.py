inputString = input("Input something ")

outputList = []
evalInteger = ""
for char in inputString:
    if char.isdigit():
        evalInteger += char
    elif evalInteger.isdigit():
        outputList.append(int(evalInteger))
        evalInteger = ""
    else:
        evalInteger = ""


print(outputList)

for i in outputList:
    print(i)