# I have a function that evaluates input, and I need to keep asking for their input and evaluating it until they enter a blank line

# while True:             # Loop continuously
#     inp = raw_input()   # Get the input
#     if inp == "":       # If it is a blank line...
#         break           # ...break the loop

# The second is like this:
number = input("Enter: ")
while number == 1:
    number = input("Enter again: ")

# Functions in small letters, classes in capital letters