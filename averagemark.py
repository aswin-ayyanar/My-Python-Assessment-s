stdmarks = {'Aswin': 85, 'Selva': 92, 'Karthi': 78, 'Balaji': 88, 'Raju': 95}
marks = list(stdmarks.values())
if marks:
    avgmarks = sum(marks) / len(marks)
else:
    avgmarks = 0
print("The average marks of the students are: ", avgmarks)