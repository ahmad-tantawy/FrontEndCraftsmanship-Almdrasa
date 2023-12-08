# Link for Planning: https://miro.com/app/board/uXjVNIBQlTs=/?moveToWidget=3458764571681656461&cot=14
# Final Project Tic Tac Toe Game Project

from tkinter import *
import random

# Function called when a button is clicked
def next_turn(row, column):
    global player, computer_turn
    computer_turn = False

    # Check if the button is empty and there is no winner yet
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[1]
            label.config(text=(player + " turn"))
            if player == players[1] and empty_spaces() > 0:
                computer_turn = True
                disable_buttons()
                window.after(650, computer_move)

        elif check_winner() is True:
            label.config(text=(players[0] + " wins"))
            update_statistics(players[0])

        elif check_winner() == "Tie":
            label.config(text="Tie!")
            update_statistics("Tie")

# Disable all buttons
def disable_buttons():
    for row in range(3):
        for column in range(3):
            buttons[row][column]['state'] = 'disabled'

# Enable all buttons
def enable_buttons():
    for row in range(3):
        for column in range(3):
            buttons[row][column]['state'] = 'normal'

# Computer's turn to make a move
def computer_move():
    global player, computer_turn
    empty_cells = []

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                empty_cells.append((row, column))

    if empty_cells:
        random_cell = random.choice(empty_cells)
        buttons[random_cell[0]][random_cell[1]]['text'] = players[1]

        if check_winner() is False:
            player = players[0]
            label.config(text=(players[0] + " turn"))

        elif check_winner() is True:
            label.config(text=(players[1] + " wins"))
            update_statistics(players[1])

        elif check_winner() == "Tie":
            label.config(text="Tie!")
            update_statistics("Tie")

        # Enable buttons after the computer's move
        computer_turn = False
        enable_buttons()

# Check if there is a winner in the current game state
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    
    elif empty_spaces() == 0:
        return "Tie"
    else:
        return False

# Count the number of empty spaces in the grid
def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    return spaces

# Update the statistics label based on the winner of the game
def update_statistics(winner):
    if winner == players[0]:
        wins_label.config(text="Player: " + str(int(wins_label["text"].split(":")[1]) + 1))
    elif winner == players[1]:
        loses_label.config(text="Computer: " + str(int(loses_label["text"].split(":")[1]) + 1))
    elif winner == "Tie":
        ties_label.config(text="Ties: " + str(int(ties_label["text"].split(":")[1]) + 1))

# Start a new game
def new_game():
    global player
    player = players[0]
    label.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="white")
window.geometry("500x650")

players = ["X", "O"]
player = players[0]

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 25), bg="white", fg="black")
label.pack(side="top", pady=10)

grid_frame = Frame(window, bd=0)
grid_frame.pack(expand=True, fill="both")

# Create buttons for each cell
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(grid_frame, text="", font=('consolas', 25), width=6, height=3,
        command=lambda row=row,column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column, padx=4, pady=4)

stats_frame = Frame(window, bd=0)
stats_frame.pack(side="bottom", pady=10)

wins_label = Label(stats_frame, text="Player: 0", font=('consolas', 15), bg="white", fg="black")
wins_label.pack(side="left", padx=10)

loses_label = Label(stats_frame, text="Computer: 0", font=('consolas', 15), bg="white", fg="black")
loses_label.pack(side="left", padx=10)

ties_label = Label(stats_frame, text="Ties: 0", font=('consolas', 15), bg="white", fg="black")
ties_label.pack(side="left", padx=10)

# Button to start a new game
new_game_button = Button(window, text="Restart", font=('consolas', 15), command=new_game)
new_game_button.pack(side="bottom", pady=10)

window.mainloop()