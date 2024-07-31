'''list = [1, 7, 3, 4, 6, 5]
print("The original list is : " + str(list))
f = True
for i in list:
    if list.count(i) > 1:
        f = False
        break
if(f):
    print("List contains all unique elements")
else:
    print("List does not contains all unique elements")'''

'''test_list = [1, 3, 4, 6, 7]
print("The original list is : " + str(test_list))
flag = True
for i in test_list:
    if test_list.count(i) > 1:
        flag = False
        break
if(flag):
    print("List contains all unique elements")
else:
    print("List does not contains all unique elements")'''
list=[1, 5, 6, 2, 3, 8, 4, 7]
n=0
for _ in list:
    n+=1
print("The length of the list is:", n)
for i in range(n):
    for j in range(0, n-i-1):
        if list[j]>list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print("Sorted list in ascending order is:", list)
