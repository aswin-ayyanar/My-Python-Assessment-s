#n = int(input("Enter a length of the list"))
mylist = []
for i in range(0,100):
    #a = input("Enter a list element")
    mylist.append(i)
    #print(mylist)
print(mylist)

for i in range(31,51):
    mylist.remove(i)

print(mylist)

print("Maximum Element",max(mylist))
print("minimum element",min(mylist))
print("sum of element",sum(mylist))
print("length element",len(mylist))

for i in mylist:
    print(i)