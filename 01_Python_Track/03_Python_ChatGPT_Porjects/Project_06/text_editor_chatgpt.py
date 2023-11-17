# Improved  (Project_06) after enhancements with ChatGPT
# Project_06 Text Editor

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    try:
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt.delete(1.0, tk.END)
            txt.insert(tk.END, text)
        window.title(f'TextEditor - {filepath}')
    except Exception as e:
        messagebox.showerror("Error", f"Error opening file: {e}")

def save_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    try:
        with open(filepath, "w") as output_file:
            text = txt.get(1.0, tk.END)
            output_file.write(text)
        window.title(f'TextEditor - {filepath}')
    except Exception as e:
        messagebox.showerror("Error", f"Error saving file: {e}")

# Dark mode color scheme
bg_color = "#202020"  # Background color
fg_color = "#FFFFFF"  # Foreground (text) color

window = tk.Tk()
window.title("TextEditor")
window.configure(bg=bg_color)

# Configure the Text widget in dark mode
txt = tk.Text(window, bg=bg_color, fg=fg_color, insertbackground=fg_color, selectbackground=fg_color)
txt.config(insertofftime=0, insertontime=0)

frame_buttons = tk.Frame(window, relief=tk.RAISED, bg=bg_color)
btn_open = tk.Button(frame_buttons, text="Open File", command=open_file, bg=bg_color, fg=fg_color)
btn_save = tk.Button(frame_buttons, text="Save As", command=save_file, bg=bg_color, fg=fg_color)

# Pack widgets
btn_open.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
btn_save.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

frame_buttons.pack(side=tk.BOTTOM, fill=tk.X)
txt.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

window.mainloop()