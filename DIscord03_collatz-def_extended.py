# # Then write  program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. 

def collatz (number):
    number = int(input("Enter a number: "))
    if int(number)%2 == 0:
        return print(f"{number} // 2" )
    else:
        return print(f"3 * {number} + 1" )

def repeat_collatz_if_not_1(number):
    while number != 1:
        collatz(number)
    


number = int(input("Enter a number: "))
repeat_collatz_if_not_1(number)




# ===============================================================


# def collatz (number):
#     while number != 1:
#         number = input("Please enter a whole number: ")
#         while number != 1:
#             number = input("Please enter a whole number: ")
#             break
    
# collatz(0)


# def collatz (number):
#     number = int(input("Enter a number: "))
#     while number%2 != 1:
#         print(f"3 * {number} + 1" )
#     return print(f"{number} // 2" )

# collatz(17)




# -------------------