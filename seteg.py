myset ={"hi",1,2,3,5.6,"Welcome",1,2}
#print(myset)
'''for i in myset:
    print(i)'''

setA = {1,2,3,4,5,6}
setB = {1,6,7,8,9,10}

unionset = setA.union(setB)
print("Union Result",unionset)

intersectset = setA.intersection(setB)
print("Intersection Result", intersectset)

diffset = setA.difference(setB)
print("Difference",diffset)

diffset1 = setB.difference(setA)
print("Difference setB-SetA",diffset1)


#setA.clear()
#print(setA)

setC = setA.copy()
print(setC)

setA.add(10)
print(setA)


setA.remove(10)
print(setA)


setA.discard(6)
print(setA)


setA.discard(11)
print(setA)

setD = {11,12,13,14}

print(setA.isdisjoint(setB))

print("SetA Elements",setA)

print("setb elements",setB)

setE = {1,2,3}
print(setA.issubset(setE))

print(setA.issuperset(setE))