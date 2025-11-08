
#input population and number of people under 18 and over 65

population=int(input("pls enter population: "))
under=int(input("enter population under 18: "))
over=int(input("enter population over 65: "))

percentage_under=under/population*100
percentage_over=over/population*100

if percentage_under>30:
    print("population is young")
elif percentage_over>25:
    print("population is aging")
elif percentage_over>20:
    print("population is young")
else:
    print("stable")   

"""
 elif percentage_over>25:
    print("population is aging")
elif percentage_over>20:
    print("population is young")
"""