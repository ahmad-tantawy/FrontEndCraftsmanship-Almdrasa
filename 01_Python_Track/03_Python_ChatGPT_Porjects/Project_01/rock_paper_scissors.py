# Link for Planing :  https://miro.com/app/board/uXjVNPgia48=/?moveToWidget=3458764569668597762&cot=14

# project_01 Rock Paper Scissors
import random

while True:
    print("Let's play Rock, Paper, Scissors against the computer!")
    user_choice = input("Choose your move ('rock', 'paper', or 'scissors'): ")

    choices = ["rock", "paper", "scissors"]
    # Validate user input
    if user_choice not in choices:
        print("Please enter a valid choice!")
        continue  # Restart the loop

    print("Computer is choosing...")
    computer_choice = random.choice(choices)

    # Compare choices
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Congratulations, you win!")
    else:
        print("Try again, the computer wins this round.")

    play_again = input("Play again? (Yes/No): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! See you next time.")
        break  # Exit the loop and end the program
