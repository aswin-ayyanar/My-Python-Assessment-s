age=int(input("Enter your age: "))
if age>18:
    status="Eligible"
elif age==18:
    status="Equal to age"
else:
    status="not Eligible"
print("You are", status, "for Vote")