import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

# Empty list to store expense data
table_data = []
# Initialize a variable to track the total row in the GUI
total_row = None

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
    date_combobox.set("2023-12-08")
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
    global table_data
    global total_row
    # Get input values
    amount = amount_entry.get()
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
    total_amount = sum(float(item["Amount"]) for item in table_data)
    # Check if a total row already exists
    if total_row:
        tree.move(total_row, "", "end")  # Move total row to end
        tree.item(total_row, values=("", "Total", total_amount, "USD"))
    else:
        # Insert a new total row at the end
        total_row = tree.insert("", "end", text="Total", values=("", "Total", total_amount, "USD"))
        tree.tag_configure("total_row", font=("bold"), background="gray")
        tree.item(total_row, tags=("total_row",))

# Clear input fields to reset the form after successfully adding an expense
def clear_input_fields(amount_entry, currency_combobox, category_combobox, date_combobox, payment_combobox):
    amount_entry.delete(0, tk.END)
    currency_combobox.set("USD")
    category_combobox.set("Life Expenses")
    date_combobox.set("2023-12-08")
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