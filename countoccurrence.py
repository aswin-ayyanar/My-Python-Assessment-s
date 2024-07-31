mylist=[1, 5, 4, 3, 5, 2, 1]
a=0
num=int(input("Enter the number that occurred to be counted:"))
for i in mylist:
    if(1==num):
        a=a+1
print("Number of times",num,"appears is",a)