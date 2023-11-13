from modules import calculate
import math
import random2

try:
    # Ask the user to enter two numbers, and enter the operation they want to perform.
    num1 = int(input("Insert your first number: "))
    num2 = int(input("Insert your second number: "))
    operation = input("Insert the operation: ")

    result = 0
    # Handle the case where the user enters an invalid operation
    if operation not in ['+', '-', '*', '/', 'power', 'pow', 'sqr', 'random']:
        print("Please choose one of these operations: +, -, *, /, power, pow, sqr and random.")
        exit()  # Exit the program
    elif operation == "+":
        result = calculate.addition(num1, num2)
    elif operation == "-":
        result = calculate.subtraction(num1, num2)
    elif operation == "*":
        result = calculate.multiplication(num1, num2)
    elif operation == "/":
        result = calculate.division(num1, num2)
    elif operation == 'power' or operation == 'pow':
        result = math.pow(num1, num2)
    elif operation == 'sqr':
        result = math.sqrt(num1)
    elif operation == 'random':   # Use random 2 module from pypi.
        result = random2.randint(num1, num2)
    print(f"result: {result}")

except ValueError:
    # Handle the case where the user enters invalid input
    print("Please try again with valid numbers.")
