# Improved  (Tic Tac Toe Game) after enhancements with ChatGPT
# Final Project Tic Tac Toe Game Project

from tkinter import Tk, Label, Button, Frame, ttk
import random

class TicTacToe:
    def __init__(self, master):
        """
        Initialize the TicTacToe game.

        Parameters:
        - master (Tk): The root Tkinter window.
        """

        background_color = "#1c313a"
        board_color = "#34495e"

        self.master = master
        self.master.title("Tic-Tac-Toe ♠")
        self.master.configure(bg=background_color)
        self.master.geometry("590x710")

        self.players = ["X", "O"]
        self.current_player = self.players[0]
        self.computer_turn = False

        # Create the GUI elements
        self.create_widgets()

    def create_widgets(self):
        """
        Create the GUI elements, such as labels, buttons, and frames.
        """
        # Label indicating the current player's turn
        self.label = Label(self.master, text=self.current_player + " turn", font=('consolas', 25), bg="#1c313a", fg="white")
        self.label.pack(side="top", pady=10)

        # Frame for the game grid
        self.grid_frame = Frame(self.master, bg="#34495e", bd=5, relief="solid", highlightbackground="#45a049", highlightthickness=2)
        self.grid_frame.pack(expand=True, fill="both")

        # 2D array to store the game buttons
        self.buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(3):
            self.grid_frame.grid_rowconfigure(i, weight=1)
            self.grid_frame.grid_columnconfigure(i, weight=1)

        # Create buttons for each cell in the game grid
        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(
                    self.grid_frame,
                    text="",
                    font=('consolas', 25),
                    width=6,
                    height=3,
                    fg="white",
                    bg="#2c3e50",
                    command=lambda row=row, column=column: self.handle_button_click(row, column)
                )
                self.buttons[row][column].grid(row=row, column=column, sticky="nsew", padx=1.5, pady=1.5)

        # Add labels for game statistics
        stats_label = Label(self.master, text="Player VS Computer", font=('consolas', 15), bg="#1c313a", fg="white")
        stats_label.pack(side="top", pady=10)

        # Frame for game statistics
        self.stats_frame = Frame(self.master, bd=0)
        self.stats_frame.pack(side="top", pady=10)  # Placed under the "Player VS Computer" label

        # Labels for displaying game statistics
        self.wins_label = Label(self.stats_frame, text="Wins: 0", font=('consolas', 12), bg="#1c313a", fg="white", width=18)
        self.wins_label.grid(row=1, column=0)

        self.loses_label = Label(self.stats_frame, text="Loses: 0", font=('consolas', 12), bg="#1c313a", fg="white", width=18)
        self.loses_label.grid(row=1, column=1)

        self.ties_label = Label(self.stats_frame, text="Ties: 0", font=('consolas', 12), bg="#1c313a", fg="white", width=18)
        self.ties_label.grid(row=1, column=2)

        developer_label = Label(self.master, text="</> by Ahmad Tantawy", fg="white", bg="#1c313a")
        developer_label.pack(side="bottom", anchor="e", pady=4, padx=6)

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#34495e")
        style.map("TButton", background=[("active", "#45a049")])

        reset_button = ttk.Button(self.master, text="Restart", command=self.start_new_game, style="TButton", width=20)
        reset_button.pack(pady=10)

    def handle_button_click(self, row, column):
        """
        Handle the button click event.

        Parameters:
        - row (int): Row index of the clicked button.
        - column (int): Column index of the clicked button.
        """
        self.computer_turn = False

        if self.buttons[row][column]['text'] == "" and not self.check_winner():
            self.buttons[row][column]['text'] = self.current_player

            if not self.check_winner():
                self.switch_turn()
                if self.current_player == self.players[1] and self.empty_spaces() > 0:
                    self.computer_turn = True
                    self.disable_buttons()
                    self.master.after(650, self.handle_computer_move)

            elif self.check_winner() is True:
                self.label.config(text=(self.players[0] + " wins"))
                self.update_statistics(self.players[0])
                self.disable_buttons()

            elif self.check_winner() == "Tie":
                self.label.config(text="Tie!")
                self.update_statistics("Tie")
                self.disable_buttons()

    def disable_buttons(self):
        """
        Disable all buttons in the game grid.
        """
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]['state'] = 'disabled'

    def enable_buttons(self):
        """
        Enable all buttons in the game grid.
        """
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]['state'] = 'normal'

    def handle_computer_move(self):
        """
        Handle the computer's move in the game.
        """
        empty_cells = [(row, column) for row in range(3) for column in range(3) if self.buttons[row][column]['text'] == ""]

        if empty_cells:
            random_cell = random.choice(empty_cells)
            self.buttons[random_cell[0]][random_cell[1]]['text'] = self.players[1]

            if not self.check_winner():
                self.switch_turn()

            elif self.check_winner() is True:
                self.label.config(text=(self.players[1] + " wins"))
                self.update_statistics(self.players[1])

            elif self.check_winner() == "Tie":
                self.label.config(text="Tie!")
                self.update_statistics("Tie")

            self.computer_turn = False
            self.enable_buttons()

            if self.check_winner() is True:
                self.disable_buttons()

    def switch_turn(self):
        """
        Switch the turn between players.
        """
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
        self.label.config(text=(self.current_player + " turn"))

    def check_winner(self):
        """
        Check if there is a winner in the current game state.

        Returns:
        - True if there is a winner.
        - "Tie" if the game is a tie.
        - False otherwise.
        """
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                self.buttons[row][0].config(bg="green")
                self.buttons[row][1].config(bg="green")
                self.buttons[row][2].config(bg="green")
                return True

        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                self.buttons[0][column].config(bg="green")
                self.buttons[1][column].config(bg="green")
                self.buttons[2][column].config(bg="green")
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.buttons[0][0].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][2].config(bg="green")
            return True
        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.buttons[0][2].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][0].config(bg="green")
            return True

        # Check for a tie
        elif self.empty_spaces() == 0:
            for row in range(3):
                for column in range(3):
                    self.buttons[row][column].config(bg="#f96006")
            return "Tie"
        else:
            return False

    def empty_spaces(self):
        """
        Count the number of empty spaces in the game grid.

        Returns:
        - The number of empty spaces.
        """
        return sum(1 for row in range(3) for column in range(3) if self.buttons[row][column]['text'] == "")

    def update_statistics(self, winner):
        """
        Update the game statistics based on the winner.

        Parameters:
        - winner (str): The winner of the game ("X", "O", or "Tie").
        """
        if winner == self.players[0]:
            self.wins_label.config(text=f"Player: {int(self.wins_label['text'].split(':')[1]) + 1}")
        elif winner == self.players[1]:
            self.loses_label.config(text=f"Computer: {int(self.loses_label['text'].split(':')[1]) + 1}")
        elif winner == "Tie":
            self.ties_label.config(text=f"Ties: {int(self.ties_label['text'].split(':')[1]) + 1}")

    def start_new_game(self):
        """
        Start a new game by resetting the game state.
        """
        self.enable_buttons()
        self.current_player = self.players[0]
        self.label.config(text=f"{self.current_player} turn")

        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="",fg="white", bg="#2c3e50")

if __name__ == "__main__":
    root = Tk()
    game = TicTacToe(root)
    root.mainloop()
