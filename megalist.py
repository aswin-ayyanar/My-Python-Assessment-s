mylist1=[1, 2, 3, 4, 5]  
mylist2=[11, 12, 13, 14, 15, 5]  
mylist3=mylist1+mylist2  
mylist3.sort()  
print("Sorted list is:",mylist3)
mylist4=[]  
for i in mylist3:  
    if i not in mylist4:  
        mylist4.append(i)   
print("Sorted list without duplicate is: ",mylist4)