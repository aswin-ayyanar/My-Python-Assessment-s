listA=[10, 20, 10, 20, 20, 30, 30, 10, 80, 40]
listB=[]
for i in listA:
    if(i not in listB):
        listB.append(i)
listA=listB
set=set(listA)
print("Set without Duplictes: ", set)