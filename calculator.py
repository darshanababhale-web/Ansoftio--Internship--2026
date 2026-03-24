# Functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Operations
print("Addition:", add(num1, num2))
print("Subtraction:", sub(num1, num2))
print("Multiplication:", mul(num1, num2))

if num2 != 0:
    print("Division:", div(num1, num2))
else:
    print("Division not possible")
