# Question 5: Creating and using a custom module


# TODO: Create a new file named 'math_operations.py' with the following content:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


# TODO: Import the custom module and use its functions
import math_operations
# im still gonna need help on this cos I half understand what I did
print("----this is your simple calculater----")
print("operations: +,-,*,/")
print("type 'quit' to exit.")
# im trying out the f key u asked

# TODO: Use a while loop to create a simple calculator
while True:
    choice = input("Input operation (+, -, *, /) or 'quit': ")
    
    if choice.lower() == 'quit':
        print("Exiting calculator. Goodbye!")
        break
if choice in ('+', '-', '*', '/'):
     num1 = float(input("Enter num1: "))
     num2 = float(input("Enter num2: "))
        
     print(f"-> Entered numbers: {num1} and {num2}")
        
if choice == '+':
     result = add(num1, num2)
     print(f"Result: {num1} + {num2} = {result}\n")
            
elif choice == '-':
     result = subtract(num1, num2)
     print(f"Result: {num1} - {num2} = {result}\n") 
            
elif choice == '*':
    result = multiply(num1, num2)
    print(f"Result: {num1} * {num2} = {result}\n") 
            
elif choice == '/':
    result = divide(num1, num2)
    print(f"Result: {num1} / {num2} = {result}\n")
else:
    print("Invalid operation. Please try again.\n")
        
