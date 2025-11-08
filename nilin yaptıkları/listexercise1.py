mystring="abcdef"
print(mystring[0])

words=[]

recordindex=0
record=-1

for i in range(5):
    
    words.append(input("enter a word: "))



for i in range(5):
    if words[i][0].isupper():
        print(words[i])
    
    if len(words[i])<record or record==-1 :
        record=len(words[i])


