a = int(input ("Enter a number: "))
factorial = 1
if a>= 1:
    for i in range (1, a+1):
        factorial=factorial *i
print("Factorial of given number is: ", factorial)