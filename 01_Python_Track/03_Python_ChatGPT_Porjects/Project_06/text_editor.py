# Link for Planning: https://miro.com/app/board/uXjVNPgia48=/?moveToWidget=3458764570177673133&cot=14
# Project_06 Text Editor

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to open a text file and display its content in the Text widget
def open_text():
    # Prompt user to select a file with a specified file type
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    # Check if a file was selected
    if filepath:
        # Open the selected file in read mode
        with open(filepath, "r") as file:
            txt.delete(1.0, tk.END)
            txt.insert(tk.END, file.read())
        
        window.title(f'TextEditor - {filepath}')

# Function to save the content of the Text widget to a text file
def save_text():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    # Check if a file was selected
    if filepath:
        with open(filepath, "w") as file:
            file.write(txt.get(1.0, tk.END))
        
        window.title(f'TextEditor - {filepath}')

# Create the main window
window = tk.Tk()
window.title("TextEditor")

# Configure the layout of the window
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=800)

# Create a Text widget for displaying and editing text
txt = tk.Text(window)

# Create a frame to hold buttons for file operations
buttons_frame = tk.Frame(window, relief=tk.RAISED)

# Create "Open" and "Save" buttons with corresponding functions
btn_open = tk.Button(buttons_frame, text="Open", command=open_text)
btn_save = tk.Button(buttons_frame, text="Save", command=save_text)

# Grid layout
btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
btn_save.grid(column=0, row=1, sticky="ew", padx=5)
buttons_frame.grid(column=0, row=0, sticky="ns")
txt.grid(column=1, row=0, sticky="nsew")

# Start the Tkinter event loop
window.mainloop()
