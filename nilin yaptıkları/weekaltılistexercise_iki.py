"""
career_satisfiction=[]
for i in range(1,6):
    score=int(input("enter score: "))
    career_satisfiction.append(score)
print(career_satisfiction)
treshold=int(input("enter treshold: "))


if treshold in career_satisfiction:
        print("index of treshold is:", career_satisfiction.index(treshold))
else:
    for i in range(1,5):
        if career_satisfiction[i]>treshold:
            print("highest index: ",i)
            career_satisfiction.pop(i)
            break
    print(career_satisfiction)
"""
"""
careers=[1,2,3,5,6]
names=["a","b","c","d","e"]

print(careers, names)
treshold=int(input("enter value: "))

if treshold in careers:
    index=careers.index(treshold)
    print("name is: ", names[index])
else:
    for i in range (1,6):
        if careers[i]>treshold:
            score=careers[i]
            careers.pop(i)
            names.pop(i)
            break
print(careers)
print(names)
"""


character_occurance=0
list_one=['ceiling','invite','solution','permanent','grant','sleeve','stereotype']
character=input("enter character: ")
print("words containing",character,":")
for word in list_one:
    if character in word:
        print(character,word,end="|")
print("words more than one",character,":")        
for word in list_one:
    for i in range(len(word)):
        letter=word[i]
        if character==letter:
            character_occurance+=1
            if character_occurance>1:
                print(word,end="|")    
                character_occurance=0
                break
    




























