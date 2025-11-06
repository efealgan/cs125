
import random
#random.randint
#discfplay values less than the value

number_list=[random.randint(1,100)]  #range(10)
number=int(input("enter value: "))

for i in range(10):

    if number< number_list[i]:
        number_list=number_list.remove(number_list)

print(number_list)



















