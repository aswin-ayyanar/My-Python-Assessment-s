mylist=[1,2,3,4,5,100,90,6]
l=len(mylist)
for i in range(1,l):
    max = 0
for mylist in mylist:
    if mylist>max:
        max=mylist
print('The largest number in list is: ', max)