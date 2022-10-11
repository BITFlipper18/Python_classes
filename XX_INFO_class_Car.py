class Car:
    def __init__(self, brand, color, fuel, tinted_windows):
        self.brand = brand
        self.color = color
        self.fuel = fuel
        self.tinted_windows = tinted_windows

    def revving(self):
        print("My car is revving pretty loudly... ")

    def horn(self):
        print('Hear that horn go TUUUUUUUUUUTTTTT!!!')

#  INSTANCES/OBJECTS OF MY CLASS
car1 = Car("BMW", "grey", "Gasoline", True)
car2 = Car("Audi", "black", "Diesel", False)

# RESULTS OF MU INSTANCES/OBJECTS
print(f"My car is a {car2.color} {car2.brand} running on {car2.fuel}!")
print(f"My car is a {car1.color} {car1.brand} running on {car1.fuel}!")

# APPLYING A METHOS TO AN INSTANCES/OBJECTS
car1.revving()
car2.horn()

# INFO AND TERMS
# - Atribute : def XXXXX (self.xxx)
# - Method call : instance1.XXXXX(value) ---> XXXXX being an atribute/method
# - PASS --> key-word to create an empty class
# - Parameters = def __init__(self, XXXXX, XXXXX)
# - Structure def __init__(self, SPEED)
#       self.choose freely = SPEED
# 



# ????? QUESTIONS ?????
# How can I create a default value in class: e.g. tinted_windows FALSE =>
# I would like to create a basic text that should easily print the results of a specific instance. Is there a way to enter a specific instance on one place, ans apply those instance values to all areas. E.g. line 22-24. only enter once "car1"-instance instead of adjusting it everywhere.?
print("----------before----------")
print(car1.color)
print("----------after----------")
