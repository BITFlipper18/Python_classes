import time

def find_it(seq):
    for i in range(0, len(seq)):
        if seq[i] % 2 == 1:
            print(f"Number {seq[i]} is odd")
            break
        else:
            print(f"array {seq[i]} is not odd")
            i += 1
    
 
array = [6, 5, 6, 5, 4, 6]

find_it(array)


# array = [6, 8, 5, 4, 8]


# for i in range(0, len(array)):
#     print(f"Number is {array[1]}!")
#     if array[i] % 2 == 1:
#         print(f"Number {array[i]} is odd")
#         break

# # AN EXAMPLE
# password = input("Enter the password: ")
# while password != "12345":
#     password = input("try again: ")
#     if password == "12345":
#         print("Correct password!")

# # OTHER EXAMPLE