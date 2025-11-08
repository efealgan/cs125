myStr = "nil"
for i in range(len(myStr)):
    if myStr[i] == myStr[len(myStr)-i-1]:
        print("True")
    else:
        print("False")