def factorial(n):
  if n == 1:
     return n
  else:
     return n*factorial(n-1)
number = int(input("Enter the number to be factoriald: "))
print("The factorial of", number, "is: ", factorial(number))