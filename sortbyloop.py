List = []
A=int(input("Enter the Total Number of List Elements: "))
for i in range(1, A+1):
    value = int(input("Enter the Value of %d Element : " %i))
    List.append(value)
for i in range (A):
    for j in range(i + 1, A):
        if(List[i] > List[j]):
            temp = List[i]
            List[i]=List[j]
            List[j]=temp
print("List in Ascending Order is : ", List)