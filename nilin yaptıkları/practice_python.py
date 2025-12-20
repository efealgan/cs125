"""
name=input("enter name: ")
age=int(input("enter age: "))
year=2025+(100-age)
number=int(input("enter number for repetition: "))
#print(("youll be 100 in the year:",year)*number)
print((f"youll be 100 in the year: {year} \n")*number)
"""
"""
number=int(input("enter number: "))
number_two=int(input("enter another number: "))
num=int(input("enter num: "))
if number%4==0:
    print("number is a multiple of 4") 
elif number%2==0:
    print("your number is even")
else:
    print("your number is odd")

if num%number_two==0:
    print("these are divisible")
else:
    print("these are not divisible")
"""
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
c=[]
number=int(input("enter number: "))
for word in a:
    if word<5:
        print(word)
        b.append(word)
print(b)

for words in a:
    if words<number:
        c.append(words)
        c.sort()
print(c)
"""
"""
number=int(input("enter number: "))
list=[]
for i in range(1,number+1):
    if number%i==0:
        list.append(i)
print(list)
"""
#exercise 5
"""
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
d=[]
for i in a and b:
    if i in a and i in b:
        c.append(i)
print(c)

list_one=[]
list_two=[]
for i in range(10):
    x=random.randint(1,100)
    y=random.randint(1,100)
    list_one.append(x)
    list_two.append(y)

print(list_one)
print(list_two)
for i in list_one and list_two: 
    if i in list_one and i in list_two:
            d.append(i)
print(d)
"""
#exercise 6
"""
word=input("enter string: ")
reversed_word=word[::-1]
if word==reversed_word:
    print("your word is palindrome")
else:
    print("your word is not palindrome")
"""
#exercise 7
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(b)

myStr = "nil"
for i in range(len(myStr)):
    if myStr[i] == myStr[len(myStr)-i-1]:
        print("True")
    else:
        print("False")
"""
#exercise 8
"""
player_one=input("enter rock, paper, scissors: ")
player_two=input("enter rock, paper, scissors: ")

if player_one==player_two:
    print("draw")
elif player_one=="rock" and player_two=="scissors":
    print("player one wins")
elif player_one=="scissors" and player_two=="rock":
    print("player two wiins")
elif player_one=="scissors" and player_two=="paper":
    print("player one wins")
elif player_one=="paper" and player_two=="scissors":
    print("player two wins")
elif player_one=="paper" and player_two=="rock":
    print("player one wins")
elif player_one=="rock" and player_two=="paper":
    print("player two wins")
else:
    print("enter again")
"""
#exercise 9
"""
import random
number=random.randint(1,9)
guess_count=0

for i in range(1,11):
    guess=int(input("guess number: "))
    if guess>number:
        print("guess too high!")
        guess_count+=1
    elif guess<number:
        print("guessed too low!")
        guess_count+=1
    elif guess==number:
        print("right guess!")
        guess_count+=1
        break
print(guess_count)
"""
#exercise 10
"""
import random
list1=[]
list2=[]
list3=[]
for i in range(1,11):
    number=random.randint(1,100)
    number2=random.randint(1,100)
    list1.append(number)
    list2.append(number2)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a and b:
    if i in a and i in b:
        c.append(i)
list1.sort()
list2.sort()
for i in list1 and list2:
    if i in list1 and i in list2:
        list3.append(i)
print(c)  
print(list1)
print(list2)  
print(list3)    
"""
#exercise 11
"""
number=int(input("enter number: "))
list=[]
isprime=True
for i in range(2,number):
    if number%i==0:
       isprime=False
       list.append(i)

if isprime:
    print("number is prime", number)
else:
    print("number is not prime, here: ",end=" ")
    print(list)
"""
#exercise 12
"""
a = [5, 10, 15, 20, 25,30,35,40,45,50]
b=[]
for i in range (0,-2,-1):
    b.append(a[i])

print(b)
"""
#exercise 15
"""
word=input("enter word with one space 3 words: ")
first_space=word.find(" ")
first_word=word[:first_space]
second_space=word.rfind(" ")
second_word=word[first_space+1:second_space]
third_word=word[second_space+1:]
print(third_word, second_word, first_word)
"""






































