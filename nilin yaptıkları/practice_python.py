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
guess=int(input("guess number: "))
guess_count=0
for i in range(1,11):
    if guess>number:
        print("guess too high!")
        guess_count+=1
    if guess<number:
        print("guessed too low!")
        guess+=1
    elif guess==number:
        print("right guess!")
        break
print(guess_count)
"""
#exercise 10
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a and b:
    if i in a and i in b:
        c.append(i)
print(c)        
"""
#exercise 11
"""
number=int(input("enter number: "))
division_count=0
for i in range(1,number+1):
    if i%number==0:
        division_count+=1
        if division_count>2:
            print("your number is not prime")
        elif division_count==2:
            print("your number is prime")
"""
#exercise 12
"""
a = [5, 10, 15, 20, 25]
b=[]
first=a[0]
last=a[-1]
b.append(first)
b.append(last)
print(b)
"""
#exercise 15
"""
word=input("enter word with one space 3 words: ")
first_space=word.find(" ")
first_word=word[:first_space]
second_space=word.find(" ", first_space+1)
second_word=[(first_space):(second_space)]
third_word=[second_space:]
print(third_word, second_word, first_word)
"""






















