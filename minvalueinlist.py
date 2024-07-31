mylist=[1,2,3,4,5,100,90,6,0]
l=len(mylist)
for i in range(1,l):
    min = 1
for mylist in mylist:
    if mylist<min:
        min=mylist
print('The smallest number in list is: ', min)