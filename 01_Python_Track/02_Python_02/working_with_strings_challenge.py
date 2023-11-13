# CHALLENGE #4
import re

# Extract from the text all times the word almdrasa is repeated,
# and the word that follows it, should that word has three letters.
text = "almdrasa is your way to learn programming the right way. almdrasa badges motivate students to do more. almdrasa quizes help students practice on what they have learned through the course. almdrasa courses are one of a kind because they were made by professionals. almdrasa look and feel is one of a kind. almdrasa wishes you a good learning. thanks."

replace_words = re.sub(r"almdrasa (\w{4,})", "Almdrasa", text, 3)

# print result
print(replace_words)
