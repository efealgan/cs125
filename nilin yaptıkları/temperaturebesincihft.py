
month=0
highest_temp=0

for i in range(1,7):
    temperature=int(input("please enter the temp: "))
    
    if temperature> highest_temp:
        highest_temp=temperature
        month+=1
print("highest temp", highest_temp, "is on the", month, ". month")



