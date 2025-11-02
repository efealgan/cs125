temperature = 0
recordTemp = 0
recordMonth = 0

for i in range(1, 13):
    temperature = float(input("What was the temperature this month?\n"))

    if temperature > recordTemp:
        recordTemp = temperature
        recordMonth = i

print("The highest temperature this year was recorded in the month number ", recordMonth, ". The temperature was ", recordTemp, "!", sep="" )