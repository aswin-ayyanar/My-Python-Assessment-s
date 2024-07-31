mylist=[1, 2, 3, 4, 5, 4, 3, 2, 1]  
print(mylist)  
otherlist=[]  
for i in mylist:  
    if i not in otherlist:  
        otherlist.append(i)   
print(otherlist)