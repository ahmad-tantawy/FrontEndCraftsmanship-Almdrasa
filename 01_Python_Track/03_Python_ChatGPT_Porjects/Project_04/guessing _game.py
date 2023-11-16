# Link for Planning: https://miro.com/app/board/uXjVNPgia48=/?moveToWidget=3458764570010964060&cot=14
# Project_04 Number Guessing Game

import random

def get_user_input(prompt, valid_values):
    """
    Function to get valid user input from a specified set of options.
    :param prompt: The prompt to display to the user.
    :param valid_values: A list of valid input values.
    :return: The user's input, converted to lowercase.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_values:
            return user_input
        else:
            print("Invalid input. Please enter a valid value.")

while True:
    attempts_number = 0  # Initialize attempts_number inside the loop

    # Get user input to start or end the game
    start = get_user_input("Do you want to play the guessing game? Yes/No: ", ["yes", "no"])
    if start == "no":
        print(f"Your score is: {attempts_number}")  # Display score
        break  # Break out of the loop if the user doesn't want to play

    while True:
        # Get user's guess
        user_guess_number = int(get_user_input("Choose a random number between '1 : 10': ", [str(i) for i in range(1, 11)]))

        compute_choice = random.randint(1, 10)

        # Compare user's guess with the randomly generated number
        while user_guess_number != compute_choice:
            if user_guess_number > compute_choice:
                print("It's higher! Try again.")
            else:
                print("It's lower! Try again.")

            attempts_number += 1
            user_guess_number = int(get_user_input("Choose a random number between '1 : 10': ", [str(i) for i in range(1, 11)]))

        print("Nice, you got it!")

        # Ask user if they want to play again
        play_again = get_user_input('Would you like to play again? Yes/No: ', ["yes", "no"])

        if play_again == "no":
            print(f"Your score is: {attempts_number}")  # Display score
            print("Hope you had a great time playing! Goodbye and have a wonderful day! 😊")
            break  # Break out of the inner loop if the user doesn't want to play again
