# Improved  (Project_05) after enhancements with ChatGPT
# Currency Converter - Project_05
import requests

API_KEY = "90f906fc2c32db9808d019b78a1462c7"

def get_input(prompt, validation_func):
    while True:
        user_input = input(prompt).upper()
        if validation_func(user_input):
            return user_input
        else:
            print(f"Please enter a valid {prompt.lower()}.")

def validate_currency_code(code):
    return code.isalpha() and len(code) == 3

def validate_positive_integer(value):
    return value.isdigit() and int(value) > 0

base_currency = get_input("initial currency to convert: ", validate_currency_code)
target_currency = get_input("target currency for conversion: ", validate_currency_code)
amount = int(get_input("amount: ", validate_positive_integer))

api_url = "http://api.exchangeratesapi.io/v1/latest"
params = {'access_key': API_KEY, 'symbols': f'{base_currency},{target_currency}'}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
    conversion_rate = data['rates'][target_currency] / data['rates'][base_currency]
    converted_amount = amount * conversion_rate
    print(f'{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}')
else:
    print(f'Error: {response.status_code}, {response.text}')
