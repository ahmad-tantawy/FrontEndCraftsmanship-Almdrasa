# CHALLENGE #2
try:
    # Ask the user: "Insert your first number: "
    first_number = float(input("Insert your first number: "))

    # Ask the user: "Insert your second number: "
    second_number = float(input("Insert your second number: "))

    # Ask the user: "Insert the operation: "
    operation = input("Insert the operation: ")

    # If the user enters an unsupported operation, print a message
    if operation not in ['+', '-', '*']:
        print("We don't support this operation")
    else:
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        else:  # Assuming operation is '*'
            result = first_number * second_number

        print("The result is:", result)

except ValueError:
    # Handle the case where the user enters invalid input
    print("Please try again with valid numbers.")

# Print "Thanks for using our software"
print('Thanks for using our software')
