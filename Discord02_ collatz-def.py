number = int(input("Enter a number: "))
def collatz (number):
    if int(number)%2 == 0:
        return print(f"{number} // 2" )
    else:
        return print(f"3 * {number} + 1" )

collatz(number)