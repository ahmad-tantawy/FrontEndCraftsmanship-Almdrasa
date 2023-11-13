# CHALLENGE #2

fruits = [
    'apples',
    'bananas',
    'grapes',
    'mangos',
    'nectarines',
    'pears',
    'watermelon',
]

# Print any sentence of your choice.
print("Hello, world! from Almdrasa.")

# Make a for loop and print each name individually.
for fruit in fruits:
    print(fruit)

# Use a while loop to print all fruits until you reach "nectarines," but don't print it.
i = 0  # Initialize the index
while fruits[i] != 'nectarines':
    print(fruits[i])
    i += 1