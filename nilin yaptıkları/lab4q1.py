
import random
num=int(random.randint(1,20))
result=0

print("the value of the die is: ", num)

for i in range(1, num+1):
    result += i
    print(i, end = " ")

if result>100:
    print("=", result, '\u2B50', end=" ")
else:
    print("=", result)    

    