
import random
numbers=[]
less_than_numbers_count=0
#Create a list containing 10 random integers between 1 and 100
#random.randint() ile istediğin sayı aralığını yaz

for i in range(10):
    numbers.append(random.randint(1,100))
print("Original list: ", numbers)

#Input a value from the user

value=int(input("Enter value: "))
print("Values less than", value, ":", end=" ")

# the numbers less than the value
#count the numbers for percentage, saymak için ilk 0 ver sonra arttır
for i in range(10):
    if numbers[i]<value:
        print(numbers[i], end=" ")
        less_than_numbers_count+=1

#(number of elements less than value / total number of elements
percentage=int((less_than_numbers_count/10)*100)
print("\nPercentage of values less than", value, ":", percentage, "%")



