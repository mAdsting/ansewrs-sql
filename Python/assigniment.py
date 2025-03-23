# Simple Calculator Program

print("Welcome to the Simple Calculator!")  # Greeting message

# Get user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

# Perform calculation
if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:  # Prevent division by zero
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation")


