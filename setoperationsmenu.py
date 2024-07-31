setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7, 8, 9}
print("Union Result: ", setA.union(setB))
print("Intersection Result SetA-SetB: ", setA.intersection(setB))
print("Intersection Result SetB-SetB: ", setB.intersection(setA))
print("Difference SetA-SetB: ", setA.difference(setB))
print("Difference setB-SetA: ", setB.difference(setA))
print("Intersection_update Result SetA-SetB: ", setA.intersection_update(setB))
print("Intersection_update Result SetB-SetA: ", setB.intersection_update(setA))
print("Difference_update SetA-SetB: ", setA.difference_update(setB))
print("Difference_update SetB-SetA: ", setB.difference_update(setA))
print("Symmetric difference: ",setA.symmetric_difference(setB))
print("Symmetric difference update: ",setA.symmetric_difference_update(setB))