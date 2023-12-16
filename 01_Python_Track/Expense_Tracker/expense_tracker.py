# Link for Planning: https://miro.com/app/board/uXjVNIBQlTs=/?moveToWidget=3458764572581882756&cot=14
# Final Project Expense Tracker

import tkinter as tk
import requests
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import date

# MY API key for https://manage.exchangeratesapi.io/
API_KEY = "90f906fc2c32db9808d019b78a1462c7"
API_URL = "http://api.exchangeratesapi.io/v1/latest"
BASE_CURRENCY = "USD"

# Empty list to store expense data
table_data = []
# Initialize a variable to track the total row in the GUI
total_row = None
# Global date
today = date.today()

# Create GUI widgets
def create_widgets(window):
    # Data entry fields
    labels = ["Amount", "Currency", "Category", "Date", "Payment Method"]
    # Grid them in the window
    for i, label_text in enumerate(labels):
        tk.Label(window, text=label_text, bg="gray").grid(row=i, column=0, padx=5, pady=5)

    amount_entry = tk.Entry(window)
    amount_entry.grid(row=0, column=1, padx=5, pady=5)

    currency_combobox = ttk.Combobox(window, values=["USD", "EUR", "JPY", "GBP", "CHF"])
    currency_combobox.grid(row=1, column=1, padx=5, pady=5)
    currency_combobox.set("USD")

    category_combobox = ttk.Combobox(window, values=["Life Expenses", "Electricity", "Gas", "Rental", "Grocery", "Savings", "Education", "Charity"])
    category_combobox.grid(row=2, column=1, padx=5, pady=5)
    category_combobox.set("Education")

    date_combobox = ttk.Combobox(window, state="readonly")
    date_combobox.grid(row=3, column=1, padx=5, pady=5)
    date_combobox.set(today)
    date_combobox.bind("<Button-1>", lambda event: open_calendar(date_combobox))

    payment_combobox = ttk.Combobox(window, values=["Cash", "Credit Card", "Paypal"])
    payment_combobox.grid(row=4, column=1, padx=5, pady=5)
    payment_combobox.set("Paypal")

    # Button and link it to the add_expense function
    ttk.Button(window, text="Add Expense", command=lambda: add_expense(amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox, tree)).grid(row=5, column=1, padx=5, pady=5)

    tree = ttk.Treeview(window, columns=("Amount", "Currency", "Category", "Date", "Payment Method"))

    # Set column attributes
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column
    tree.column("Amount", width=100, anchor=tk.CENTER)
    tree.column("Currency", width=100, anchor=tk.CENTER)
    tree.column("Category", width=100, anchor=tk.CENTER)
    tree.column("Date", width=100, anchor=tk.CENTER)
    tree.column("Payment Method", width=100, anchor=tk.CENTER)

    # Set column headings
    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("Amount", text="Amount")
    tree.heading("Currency", text="Currency")
    tree.heading("Category", text="Category")
    tree.heading("Date", text="Date")
    tree.heading("Payment Method", text="Payment Method")

    tree.grid(row=7, column=0, columnspan=5, padx=5, pady=5)

    return amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox, tree

# Open a calendar for date selection
def open_calendar(date_combobox):
    top = tk.Toplevel()
    cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=10)
    ttk.Button(top, text="Select Date", command=lambda: on_date_selected(cal, top, date_combobox)).pack(pady=10)

# Handle date selection from the calendar
def on_date_selected(cal, top, date_combobox):
    date_combobox.set(cal.get_date())
    top.destroy()

# Add an expense to the table
def add_expense(amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox, tree):
    # Get input values
    amount = amount_entry.get()
     # Check if the amount is a valid number
    try:
        float(amount)
    except ValueError:
        # Display an error message
        messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
        return
    currency = currency_combobox.get()
    category = category_combobox.get()
    date = date_combobox.get()
    payment_method = payment_combobox.get()

    # Input fields are filled
    if amount and currency and category and date and payment_method:
        # Insert the expense into the Treeview widget
        tree.insert("", "end", values=(amount, currency, category, date, payment_method))
        # Update the data
        table_data.append({"Amount": amount, "Currency": currency, "Category": category, "Date": date, "Payment Method": payment_method})
        # Update the total amount
        update_total_amount(tree)
        # Clear input fields
        clear_input_fields(amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox)

# Update the total amount in the Treeview
def update_total_amount(tree):
    global total_row

    total_amount = do_conversion(table_data)
    # Check if a total row already exists
    if total_row:
        tree.move(total_row, "", "end")  # Move total row to end
        tree.item(total_row, values=(total_amount, "USD"))
    else:
        # Insert a new total row at the end
        total_row = tree.insert("", "end", text="Total", values=(total_amount, "USD"))
        tree.tag_configure("total_row", font=("bold"), background="gray")
        tree.item(total_row, tags=("total_row",))

    # Scroll to the Total row when table became more biger
    tree.see(tree.get_children()[-1])

def get_amount_and_currency(table_data):
    for entry in table_data:
        amount = float(entry.get('Amount', 0))
        currency = entry.get('Currency', 'N/A')
        yield amount, currency

def convert_to_usd(amount, base_currency):
    params = {
        "access_key": API_KEY,
        "symbols": f'{base_currency},{BASE_CURRENCY}'
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        conversion_rate = data['rates'][BASE_CURRENCY] / data['rates'][base_currency]

        converted_amount = round(amount * conversion_rate, 2)  # Limit to two digits after the decimal point
        return converted_amount
    else:
        return None

def do_conversion(table_data):
    converted_data = []

    for amount, currency in get_amount_and_currency(table_data):
        if currency != BASE_CURRENCY:
            converted_amount = convert_to_usd(amount, currency)
            if converted_amount is not None:
                converted_data.append((converted_amount, BASE_CURRENCY))
        else:
            converted_data.append((amount, currency))

    total = sum(amount for amount, _ in converted_data)
    return total

# Clear input fields to reset the form after successfully adding an expense
def clear_input_fields(amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox):    
    amount_entry.delete(0, tk.END)
    currency_combobox.set("USD")
    category_combobox.set("Education")
    date_combobox.set(today)
    payment_combobox.set("Paypal")

window = tk.Tk()
window.title("Expense Tracker")
window.configure(bg="lightgray")
window.geometry("540x460")

# Create GUI widgets
widgets = create_widgets(window)
amount_entry = widgets[0]
currency_combobox = widgets[1]
category_combobox = widgets[2]
date_combobox = widgets[3]
payment_combobox = widgets[4]
tree = widgets[5]

# Event loop
window.mainloop()