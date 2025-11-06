
score_list=[]
tresholdnotmet= True

for i in range(5):
    scores=score_list.append(int(input("enter a score from 1 to 100: ")))
print(score_list)

treshold=int(input("input the satisfiction treshold: "))

for i in range(5):
    if treshold== score_list[i]:
        n=score_list.index(treshold)
        print(n)
        tresholdnotmet=False
    
if tresholdnotmet:    
    score_list_sorted=score_list
    score_list_sorted.sort()

    for i in range(5):
        if score_list_sorted[i]>treshold:
            print("removing element at index", i)
            score_list.remove(score_list_sorted[i])
            print(score_list)
            break


    











    """
    elif score_list[i]> treshold:
        removed_one=i
        new_list=score_list.remove(i)
    """


