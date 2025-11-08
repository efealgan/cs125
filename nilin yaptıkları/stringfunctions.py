
name=input("pls enter your name: ")

name_len=len(name)
print("ur name is: ", name, "and has", name_len, "charahcters")

count_a=name.count("a")
print("your name has", count_a, "a letters")

start=name.find("efe")
print("your name starts at: ", start, "letter")

end=name.rfind("algan")
print("your surname appears at",end, "th letter")

upper=name.replace("efe", "EFE")
print("ur new name is: ", upper)

spaceless=name.strip()
print("your new new name is: ", spaceless)

