
first_half=[]
last_half=[]


n=int(input("how many names: "))

for i in range(n):
    name=input("enter name: ")
    if "a"<=name[0].lower()<="m":
        first_half.append(name)
        
    if "n"<=name[0].lower()<="z":
        last_half.append(name)
first_half.sort()
last_half.sort()

print(first_half, last_half)


