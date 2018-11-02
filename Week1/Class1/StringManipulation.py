# This will convert text to lowercase and uppercase and then concatenate text and variables into one final string.

first_name = "Brendan"
last_name = "Wood"
number = 42

result = "My name is " + first_name.lower() + " " + last_name.upper() + ", and my favourite" \
    + " number is " + str(number) + "."

print(result)
