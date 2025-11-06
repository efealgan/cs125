"""
height=1080
width=1920
new_width=1280
new_height=(height/width)*new_width
print("the new height should be: ", float(new_height), "pixels")
"""
"""
pressure=int(input("enter pressure: "))
coping=int(input("enter coping: "))
stress=float(pressure/coping)
print("stress rating: ", round(stress,2))
"""
"""
price=int(input("enter price: "))
a=100
b=2
quantity_demanded=a-(b*price)
print("estimated demand: ", quantity_demanded)
"""
"""
sentence=input("enter sentence: ")
print("first character: ", sentence[0])
print("last character: ", sentence[-1])
first_space=sentence.find(" ")
last_space=sentence.rfind(" ")
first_word=sentence[: first_space].upper()
last_word=sentence[last_space:].upper()
print("uppercase words:",last_word,first_word, sep="")
print(sentence.replace(" ", ""))
"""
"""
info=input("enter country and last visited: ")
country=info[ :info.find(" ")]
year=info[info.find(" "): ]
last_visit=2025-int(year)
print("it has been", last_visit, "years since you last visited",country)
"""
"""
name=input("enter research: ")
year=input("enter year: ")
participant=input(f"enter number in {name} at start and end of {year}:")
start_participant=int(participant[ : participant.find(" ")])
end_participant=int(participant[participant.rfind(" "): ])
growth_rate=float((end_participant-start_participant)/start_participant*100)
print(f"participant growth rate for {name} is {growth_rate} %")
"""
"""
apple=int(input("enter total number of apples: "))
price=float(input("enter price of kg of apples: "))
total_price=apple*price
if apple>50:
    total_price+=100

print("your total earning is: ", total_price)
"""
"""
apple=int(input("enter total number of apples: "))
price=float(input("enter price of kg of apples: "))
total_price=apple*price
if apple<=50:
    total_price=apple*price
else:
    total_price=price*50+(apple-50)*1.5*price
print("earning is: ", total_price,"$")
"""
"""
character=input("enter a consonant: ")
if character.lower() in"a,e,i,o,u":
    print("the letter is a vowel")
else:
    print("your letter is a consonent")
"""
"""
import random
number=random.randint(1,9)
guess=int(input("guess: "))
if guess==number:
    print("well guessed")
else:
    print("wrong guess")
"""
"""
word=input("emter sentence: ")
first=word[0]
last=word[-1]
if first==last:
    print("yay")
else:
    print("nay")
"""
"""
grade=int(input("enter grade: "))
if grade>100:
    print("wrong grade")
elif grade>90:
    print("u r A")
elif grade>80:
    print("u r B")
elif grade>70:
    print("u r C")
elif grade>60:
    print("u r D")
elif grade<=60:
    print("u r F")
print("done")
"""
"""
population=int(input("enter population: "))
old=int(input("enter people over 65: "))
young=int(input("enter people under 18: "))
percentage_old=old/population*100
percentgae_young=young/population*100
if percentgae_young>30:
    print("pop is young")
elif percentage_old>25:
    print("pop is aged")
elif percentage_old>20:
    print("pop is aging")
else:
    print("stable")
"""
"""
number=int(input("enter number: "))
if number%2==0:
    print("ur number is even")
else:
    print("your number is odd")
"""
"""
year=int(input("enter a year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not leap year")
"""
"""
number1=int(input("enter number1: "))
number2=int(input("enter number2: "))
number3=int(input("enter number3: "))
largest_number=0
if number1>number2 and number1>number3:
    largest_number=number1
elif number2>number3 and number2>number1:
    largest_number=number2
elif number3>number1 and number3>number2:
    largest_number=number3   
print("largest number is:", largest_number)
"""
"""
time=int(input("enter time: "))
if time<1200:
    print("good morning")
elif 1200<=time<=1800:
    print("good afternoon")
elif time>1800:
    print("good evening")
"""
"""
step=int(input("enter nujmber of steps: "))
if step<5000:
    print("inactive- should take", 10000-step,"more")
elif 5000<=step<=7499:
    print("low active- should take",10000-step,"more")
elif 7500<=step<=9999:
    print("moderately active*should take",10000-step,"more")
elif step>=10000:
    print("active- congrats!")
"""
"""
number=int(input("enter number: "))
if number>0:
    print("positive")
elif number<0:
    print("negative")
elif number==0:
    print("zero")
"""
"""
temp=int(input("enter temperature: "))
if temp<10:
    print("cold")
elif 10<=temp<=25:
    print("warm")
elif temp>25:
    print("warm")
"""
"""
movie=input("enter movie name: ")
smiley=int(input("enter smiley bw 1-5: "))
if smiley>5 or 1>smiley:
    print("movie program finished...")
else:
    print(movie,":", smiley* ("\U0001F603"))
    print("movie program finisjed")
"""
"""
height=int(input("enter height:"))
width=int(input("enter width: "))
carpet=18
room=float(height*width)
if room*0.6<carpet<=room*1:
    print("carpet is suitable area", room,"sqm")
else:
    print("carpet is not suitable area", room,"sqm")
"""
"""
annual_income=int(input("enter income: "))
dependents=int(input("number of dependents: "))

if dependents==0:
    print("not eligible for aid")
elif annual_income<3000:
    print("total aid is: ",float(2000*dependents))
elif 3000<=annual_income<=5000:
    print("total aid is: ",float(1500*dependents))
elif annual_income>5000:
    print("total aid is: ",float(1000*dependents))
"""
"""
participant_vanilla=0
participant_choc=0
age_total=0
for i in range(5):
    flavour=input("enter c or v: ")
    age=int(input("enter age: "))
    if flavour.lower()=="v":
        participant_vanilla+=1
    elif flavour.lower()=="c":
        participant_choc+=1
    age_total+=age
print("average is: ", age_total/5)
print("vanilla: ", participant_vanilla)
print("choc: ", participant_choc)
"""
"""
highest_temp=0
month_number=0
for i in range(1,6):
    temp=int(input("enter temp: "))
    if temp>highest_temp:
        highest_temp=temp
        month_number=i
print("highest temp in month", month_number, "is", highest_temp)
print("yippiii")
"""
"""
sentence=input("enter sentence: ")
vowel_count=0
vowel="aeiou"
for i in sentence:
    if i.lower() in vowel:
        vowel_count+=1
print("number of voewls: ", vowel_count)
"""
#week5 slide 14 and continue
"""
import random
secret=random.randint(1,10)
for i in range(1,4):
    guess=int(input("guess number: "))
    if secret==guess:
        print("correct guess")
        break
    else:
        print("you lose")
print("the nmbr is: ", secret)
"""
"""
number=0
for i in range (1,11):
    number+=1
    print(number**2, end=" ")
"""
"""
#########################################
prime = True #assume true
number = int(input("provide a positive integer"))
if number == 1:
    prime = False
elif number > 0:
    for i in range(2, number):
        if number%i == 0:
            print("The number you provided (", number, ") isn't a prime number. It can be divided to:", i)
            prime = False
            break
else:
    print("You didn't provide a positive integer.")
    prime = False
if prime:
    print(number, "is  a prime number.")
# else:
#     print(number, "is a prime number.")
"""
"""
# a < b < c | true
alphabet = "abcdefghijklmnopqrstuvwxyz"
inputString = input("say something ")
inputString = inputString.lower()
yippi = True
for i in range(len(inputString)-1):
    letter = inputString[i]
    if not letter in alphabet:
        print("Encountered non-alphabetical character: \"", letter,"\" skipping.", sep="")
        continue
    elif  letter > inputString[i+1]: # is NOT in alphabetical order
        print(letter, "and", inputString[i+1],"are not in alphabetical order.")
        yippi = False 
        break
if yippi:
    print("your sentence was in alphabetical order!!!!")
"""
"""
same_counter=0
for i in range(1,6):
    word=input("enter a word: ")
    if word[0].lower()==word[-1].lower():
        print(word," starts and ends with the same letter")
        same_counter+=1
percentage=float((same_counter/5)*100)
print(percentage,"%", "words start and end with the samcar==e letter")
"""
"""
total_fee=0
fee_geeral=0
for i in range(1,6):
    car=input("enter type: ")
    days=int(input("enter nmber of days: "))
    if car== "s" or car== "S":
        total_fee=130*days
        fee_geeral+=total_fee
    elif car== "m" or car== "M":
        total_fee=165*days
        fee_geeral+=total_fee
    elif car== "l" or car== "L":
        total_fee=220*days
        fee_geeral+=total_fee
    print("customer",i, "total: ",total_fee)
print("total or all rentas: ", fee_geeral)
"""
"""
multiply=0
for i in range (1,13):
    multiply=7*i
    print(multiply,end=" ")
"""
"""
start=int(input("enter sat number: "))
end=int(input("enter end nuber: "))
even_counter=0
print("the numbers are: ",end=" ")
for number in range(start,end+1):
    if end<start:
        print("enter again")
    elif 10<number<end and number%2==0:
        even_counter+=1
        print(number, end=" ")
        
print("there are",even_counter,"numbers greater than 10 in the range")
"""
"""
import random
secret=random.randint(1,20)
guess=False
for i in range(1,6):
    guess=int(input("guess: "))
    if guess==secret:
        print("yay, guess in ", i,"tries")
        guess=True
        break
    elif guess>secret:
        print("ur guess is too high")
        guess=False
    elif guess<secret:
        print("ur guess is too low")
        guess= False
if not guess:   
    print("fail, the number was: ", secret)
"""       
"""
l=[1,2,3,4,5]
total=0
for i in l:
    total+=i
print(total)
l.append(6)
print(l)
"""
"""
l=[1,2,3,4,5]
l.insert(3,6)
print(l)
"""
"""
friends = ['Harry','Emily','Bob','Jane', 'Emily']
n = friends.index( 'Emily' )
print( n )
n = friends.index( 'Emily', n+1 )
print( n )

friends.pop(3)
print(friends)

friends.remove("Bob")
print(friends)
"""
"""
list=[]
for i in range(1,6):
    word=input("enter word: ")
    list.append(word)
shortest=list[0]
print(list)
for word in list:
    if word[0]==word[0].upper():
        print("uppercase ones: ",word)
for word in list:
    if len(word)<len(shortest):
        shortest=word
print("shortest is: ",shortest)
"""



























































