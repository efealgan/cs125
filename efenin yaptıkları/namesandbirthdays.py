names = ["Ayşe", "Oliver", "Mehmet","Emily", "Elif"]
birthyears = [2002, 2001, 2005, 2015, 1999]
foundTheName = False

queryName = input("Enter a name: ")

for i in range(len(names)):
    if names[i] == queryName: #name was in the list
        yearOfBirth = birthyears[i]
        print(queryName, " was born in ", yearOfBirth, ".", sep="")
        names.pop(i)
        birthyears.pop(i)
        print("Updated data: ", names, birthyears)
        foundTheName = True
        break

if not foundTheName:
    print(queryName, " not found in the list!", sep="")


