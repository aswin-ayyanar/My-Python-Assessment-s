class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")
a=float(input("Enter the number: "))
b=float(input("Enter the number: "))
calculator = Calculator()
result = calculator.add(a, b)
print("a + b =", result)
result = calculator.subtract(a, b)
print("a - b =", result)
result = calculator.multiply(a, b)
print("a * b =", result)
result = calculator.divide(a, b)
print("a / b =", result)
result = calculator.divide(a, b)
print("a / b =", result)