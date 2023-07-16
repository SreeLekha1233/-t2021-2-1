# Getting input from the user
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operation = input("Enter the type of operation (+, -, *, /): ")

# Performing the selected operation
result = None
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation.")

# result
print("Result:", result)
