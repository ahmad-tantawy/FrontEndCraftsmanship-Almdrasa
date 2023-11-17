# Link for Planning: https://miro.com/app/board/uXjVNPgia48=/?moveToWidget=3458764570048853300&cot=14
# Project_05  Currency Converter

import requests

# MY API key for https://manage.exchangeratesapi.io/
API_KEY = "90f906fc2c32db9808d019b78a1462c7"

def get_positive_integer_input(prompt):
    # Function to get a positive integer from the user with input validation
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def get_currency_input(prompt):
    # Function to get a valid 3-letter currency code from the user with input validation
    while True:
        currency = input(prompt).upper()  # Convert to uppercase for consistency
        if currency.isalpha() and len(currency) == 3:
            return currency
        else:
            print("Please enter a valid 3-letter currency code.")

def do_conversion():
    # Get user inputs
    base_currency = get_currency_input("Please enter initial currency to convert: ")
    target_currency = get_currency_input("Please enter target currency for conversion: ")
    amount = get_positive_integer_input("Please enter amount: ")

    # Make API request to apilayer
    api_url = "http://api.exchangeratesapi.io/v1/latest"

    params = {
        'access_key': API_KEY,
        'symbols': f'{base_currency},{target_currency}',
    }

    print("Processing your request. Please wait...")
    response = requests.get(api_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        conversion_rate = data['rates'][target_currency] / data['rates'][base_currency]
        converted_amount = amount * conversion_rate
        print(f'{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}')
    else:
        print(f'Error: {response.status_code}, {response.text}')

# I Includeted this in the planning phase to ask user if he wants another conversion
def main():
    while True:
        do_conversion()
        another_conversion = input("Do you want to make another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break

if __name__ == "__main__":
    main()