# Improved  ( Expense Tracker ) after enhancements with ChatGPT
# Final Project Expense Tracker

import tkinter as tk
import requests
from tkinter import ttk, messagebox, Label
from tkcalendar import Calendar
from datetime import date
import asyncio

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

# Cached exchange rates
exchange_rates_cache = {}

# Create GUI widgets
def create_widgets(window):
    """
    Create and configure the user interface widgets for the expense tracker.

    Parameters:
        window (tk.Tk): The main Tkinter window.

    Returns:
        tuple: A tuple containing the created Tkinter Entry and Combobox widgets, and the Treeview widget.

    This function sets up the user interface components including data entry fields,
    a button, a frame for displaying a treeview, and labels. It uses the Tkinter and ttk
    modules for creating GUI elements.

    Args:
        window (tk.Tk): The main Tkinter window where the widgets will be placed.

    Returns:
        tuple: A tuple containing the following widgets in order:
            - amount_entry (tk.Entry): Tkinter Entry widget for entering the expense amount.
            - currency_combobox (ttk.Combobox): ttk.Combobox widget for selecting the currency.
            - category_combobox (ttk.Combobox): ttk.Combobox widget for selecting the expense category.
            - date_combobox (ttk.Combobox): ttk.Combobox widget for selecting the expense date.
            - payment_combobox (ttk.Combobox): ttk.Combobox widget for selecting the payment method.
            - tree (ttk.Treeview): ttk.Treeview widget for displaying and managing expenses.
    """
    # Data entry fields
    labels = ["Amount", "Currency", "Category", "Date", "Payment Method"]

    # Grid labels in the window
    for i, label_text in enumerate(labels):
        tk.Label(window, text=label_text, bg="#1c312a", fg="white").grid(row=i, column=0, padx=50, pady=5, sticky="w")

    # Entry and Combobox widgets
    amount_entry = tk.Entry(window, width=31, bg="#34499e", fg="white")
    amount_entry.grid(row=0, column=1, padx=0, pady=5)

    currency_combobox = ttk.Combobox(window, width=28, values=["USD", "EUR", "JPY", "GBP", "CHF"])
    currency_combobox.grid(row=1, column=1, padx=5, pady=5)
    currency_combobox.set("USD")

    category_combobox = ttk.Combobox(window, width=28, values=["Life Expenses", "Electricity", "Gas", "Rental", "Grocery", "Savings", "Education", "Charity"])
    category_combobox.grid(row=2, column=1, padx=5, pady=5)
    category_combobox.set("Education")

    date_combobox = ttk.Combobox(window, width=28, state="readonly")
    date_combobox.grid(row=3, column=1, padx=5, pady=5)
    date_combobox.set(today)
    date_combobox.bind("<Button-1>", lambda event: open_calendar(date_combobox))

    payment_combobox = ttk.Combobox(window, width=28, values=["Cash", "Credit Card", "Paypal"])
    payment_combobox.grid(row=4, column=1, padx=5, pady=5)
    payment_combobox.set("Paypal")

    # Create a frame for the treeview with a border
    add_button = ttk.Button(window, text="Add Expense  ▼", command=lambda: add_expense(amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox, tree))
    add_button.grid(row=5, column=1, pady=5, padx=5)

    # Create a frame for the treeview with a border
    tree_frame = tk.Frame(window, borderwidth=3, relief="solid", highlightbackground="#34499e", highlightthickness=3)
    tree_frame.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Create the treeview inside the frame
    tree = ttk.Treeview(tree_frame, columns=("Amount", "Currency", "Category", "Date", "Payment Method"))

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

    tree.grid(row=0, column=0, sticky="nsew")  # Adjust row and column based on your layout

    developer_label = Label(window, text="</> by Ahmad Tantawy", fg="white", bg="#1c313a")
    developer_label.grid(row=8, column=0, columnspan=5, pady=1, padx=8, sticky="se")

    return amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox, tree

# Open a calendar for date selection
def open_calendar(date_combobox):
    """
    Open a calendar for date selection.

    Parameters:
        date_combobox (ttk.Combobox): The ttk.Combobox widget associated with the date selection.

    This function creates a new Tkinter Toplevel window containing a calendar widget for selecting a date.
    The selected date is then inserted into the specified ttk.Combobox widget.

    Args:
        date_combobox (ttk.Combobox): The ttk.Combobox widget where the selected date will be inserted.

    """
    # Create a new Toplevel window for the calendar
    top = tk.Toplevel()

    # Create a Calendar widget with day selection mode and a custom date pattern
    cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=10)

    # Button to confirm and insert the selected date into the associated Combobox
    ttk.Button(top, text="Select Date ▼", command=lambda: on_date_selected(cal, top, date_combobox)).pack(pady=20, padx=20)

# Handle date selection from the calendar
def on_date_selected(cal, top, date_combobox):
    """
    Handle date selection from the calendar.

    Parameters:
        cal (Calendar): The Calendar widget for date selection.
        top (tk.Toplevel): Toplevel window with the Calendar.
        date_combobox (ttk.Combobox): Combobox for displaying the selected date.

    Sets the selected date from the Calendar to the Combobox and closes the Toplevel window.

    """
    date_combobox.set(cal.get_date())
    top.destroy()

# Add an expense to the table
def add_expense(amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox, tree):
    """
    Add an expense to the Treeview widget.

    Parameters:
        amount_entry (tk.Entry): Entry widget for amount input.
        currency_combobox (ttk.Combobox): Combobox for currency selection.
        category_combobox (ttk.Combobox): Combobox for category selection.
        date_combobox (ttk.Combobox): Combobox for date selection.
        payment_combobox (ttk.Combobox): Combobox for payment method selection.
        tree (ttk.Treeview): Treeview widget to display expense entries.

    Adds an expense entry to the Treeview, updates the data, and clears the input fields.
    """
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
    """
    Update the total amount in the Treeview.

    Parameters:
        tree (ttk.Treeview): Treeview widget containing expense entries.

    Updates the total amount row in the Treeview based on the current data.

    """
    global total_row

    total_amount = do_conversion(table_data)
    # Check if a total row already exists
    if total_row:
        tree.move(total_row, "", "end")  # Move total row to end
        tree.item(total_row, values=(total_amount, "USD"))
    else:
        # Insert a new total row at the end
        total_row = tree.insert("", "end", text="Total", values=(total_amount, "USD"))
        tree.tag_configure("total_row", font=("bold"), background="#34499e", foreground="white")
        tree.item(total_row, tags=("total_row",))

    # Scroll to the Total row when the table becomes larger
    tree.see(tree.get_children()[-1])


def get_amount_and_currency(table_data):
    """
    Extracts amounts and currencies from the table data.

    Parameters:
        table_data (list): List of dictionaries containing expense data.

    Yields:
        tuple: A tuple containing the amount (float) and currency (str).

    """
    for entry in table_data:
        amount = float(entry.get('Amount', 0))
        currency = entry.get('Currency', 'N/A')
        yield amount, currency

async def convert_to_usd_async(amount, base_currency):
    """
    Asynchronously converts an amount from the given base currency to USD.

    Parameters:
        amount (float): The amount to convert.
        base_currency (str): The currency of the amount.

    Returns:
        float: The converted amount in USD.
    """
    if base_currency == BASE_CURRENCY:
        return amount

    if (amount, base_currency) in exchange_rates_cache:
        conversion_rate = exchange_rates_cache[(amount, base_currency)]
    else:
        params = {
            "access_key": API_KEY,
            "symbols": f'{base_currency},{BASE_CURRENCY}'
        }

        response = await loop.run_in_executor(None, lambda: requests.get(API_URL, params=params))

        if response.status_code == 200:
            data = response.json()
            conversion_rate = data['rates'][BASE_CURRENCY] / data['rates'][base_currency]
            exchange_rates_cache[(amount, base_currency)] = conversion_rate
        else:
            print(f'Error: {response.status_code}, {response.text}')
            return None

    converted_amount = round(amount * conversion_rate, 2)  # Limit to two digits after the decimal point
    return converted_amount

async def do_conversion_async(table_data):
    """
    Asynchronously calculates the total amount in USD for a list of entries.

    Parameters:
        table_data (list): A list of dictionaries representing expense entries.

    Returns:
        float: The total amount in USD.
    """
    tasks = [convert_to_usd_async(amount, currency) for amount, currency in get_amount_and_currency(table_data)]
    results = await asyncio.gather(*tasks)

    total = sum(results)
    return total

def do_conversion(table_data):
    """
    Synchronously calculates the total amount in USD for a list of entries.

    Parameters:
        table_data (list): A list of dictionaries representing expense entries.

    Returns:
        float: The total amount in USD.
    """
    loop = asyncio.get_event_loop()
    total = loop.run_until_complete(do_conversion_async(table_data))
    return total

# Clear input fields to reset the form after successfully adding an expense
def clear_input_fields(amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox):
    """
    Clears the input fields in the expense form.

    Parameters:
        amount_entry (tk.Entry): The Entry widget for the amount.
        currency_combobox (ttk.Combobox): The Combobox widget for selecting currency.
        category_combobox (ttk.Combobox): The Combobox widget for selecting category.
        date_combobox (ttk.Combobox): The Combobox widget for selecting the date.
        payment_combobox (ttk.Combobox): The Combobox widget for selecting the payment method.
    """
    amount_entry.delete(0, tk.END)
    currency_combobox.set("USD")
    category_combobox.set("Education")
    date_combobox.set(today)
    payment_combobox.set("Paypal")

# Create the main Tkinter window
window = tk.Tk()
window.title("Expense Tracker ❖")
window.configure(bg="#1c313a")
window.geometry("524x464")

# Create GUI widgets using the create_widgets function
widgets = create_widgets(window)
amount_entry = widgets[0]
currency_combobox = widgets[1]
category_combobox = widgets[2]
date_combobox = widgets[3]
payment_combobox = widgets[4]
tree = widgets[5]

# Create an event loop for async functions
loop = asyncio.get_event_loop()

# Start the Tkinter main event loop
window.mainloop()

# Close the asyncio event loop after the Tkinter window is closed
loop.close()