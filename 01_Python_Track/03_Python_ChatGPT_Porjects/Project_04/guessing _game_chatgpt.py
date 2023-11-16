# Improved Number guessing game (Project_04) after enhancements with ChatGPT
import random

def get_user_input(prompt, valid_values):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_values:
            return user_input
        print("Invalid input. Please enter a valid value.")

def play_guessing_game():
    attempts_number = 0

    start = get_user_input("Do you want to play the guessing game? Yes/No: ", ["yes", "no"])
    if start == "no":
        print(f"Your score is: {attempts_number}")
        return

    while True:
        user_guess = int(get_user_input("Choose a random number between 1 and 10: ", [str(i) for i in range(1, 11)]))
        target_number = random.randint(1, 10)

        while user_guess != target_number:
            print("It's higher! Try again." if user_guess > target_number else "It's lower! Try again.")
            attempts_number += 1
            user_guess = int(get_user_input("Choose a random number between 1 and 10: ", [str(i) for i in range(1, 11)]))

        print("Nice, you got it!")

        play_again = get_user_input('Would you like to play again? Yes/No: ', ["yes", "no"])
        if play_again == "no":
            print(f"Your score is: {attempts_number}")
            print("Hope you had a great time playing! Goodbye and have a wonderful day! 😊")
            break

if __name__ == "__main__":
    play_guessing_game()
