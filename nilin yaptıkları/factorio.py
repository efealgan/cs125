import math

copper=float(input("pls enter the number of copper you have in your map: "))

coal=float(input("pls enter the amount of coal you have in your map: "))

tree=float(input("do you have trees in your map? how much? "))

print("you have this much of copper ", copper, "you have this much of coal ", coal, "you have this much of trees ", tree)

if copper<15:
    print("you are kinda doomed with copper, look for coal")

if copper>15:
    print("you are not doomed with copper but look for coal")

if coal<43892:
    print("you are good to go with coal but look for trees")

if coal>43892:
    print("you are doomed with coal but go and check the trees")

if tree>99999:
    print("you are liviiiiinnnnnggggg with treeessss")

if tree<99999:
    print("oh noooo u r dead without treeesss")

print("if you are not doomed in all three, you win the game yipppiiiiiiiii")