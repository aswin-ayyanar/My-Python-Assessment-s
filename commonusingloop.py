L1=[16, 20, 33, 49, 54]
L2=[54, 22, 65, 16, 92]
L3=[]
for i in L1:
    for j in L2:
        if i==j:
            L3.append(i)
print("Common Element: ", L3)