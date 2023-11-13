# CHALLENGE #5

# Import the regular expression module
import re

# Define input and output file paths
input_file_path = "strings.txt"
output_file_path = "string_output.txt"

# Open input and output files in read and write text mode respectively
with open(input_file_path, "rt") as strings_file, open(output_file_path, "wt") as output_file:
    print("Start reading from file")

    result = ""
    for line in strings_file:
        if line.strip() == "I":
            # Append the stripped line with a space to the result
            result += line.strip() + " "
        elif line.strip() == "Almdrasa":
            # Append the stripped line with a space to the result
            result += line.strip() + " "
        else:
            # Convert the stripped line to lowercase and append with a space to the result
            result += line.strip().lower() + " "

    # Print the result to the output file
    print(result, file=output_file)

# Print a completion message
print("I am done!")
