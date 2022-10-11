import math

def cost_per_square_inch(pizza_diameter_in_inch, price_in_USD):
    square_inch_of_pizza = (math.pi*((pizza_diameter_in_inch/2)**2))
    cost_per_square_inch = round((price_in_USD / square_inch_of_pizza), 2)
    print(f"The cost per square inch for this pizza is {cost_per_square_inch} USD! Try to enjoy it now!")

diameter_in_inch = float(input("Enter your pizza's diameter in inches: "))
price_in_USD = float(input("Enter your pizza's cost price in USD: "))

cost_per_square_inch(diameter_in_inch, price_in_USD)