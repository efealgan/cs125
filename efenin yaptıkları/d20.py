import random

result = 0
#roll = random.randint(1,20)
roll = 18
print("Rolled", roll)

for i in range(1, roll+1):
    result += i
    print(i, end = " ")

print("=", result)








