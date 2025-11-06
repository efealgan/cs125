
start=int(input("enter starting number: "))
end=int(input("enter ending number: "))
sum_of_odd=0
odd_counter=0

for i in range(start, end+1):
    if not(i%5) and not(i%7):
        print(i, "is divisible by 5 and 7! loop exiting...")
        break

    if i%2: #if i is odd
        sum_of_odd+=i
        odd_counter+=1    

   
average=sum_of_odd/odd_counter
print(average)


    