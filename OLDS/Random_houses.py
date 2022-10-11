from random import random
import turtle as turtle
from utils.usefull_functions import teken_huis
import random

coordinaten = [0]

nieuw_punt = 0
nieuw_punt_x = 0
nieuw_punt_y = 0

Xpunten = [0]
Ypunten = [0]

# def teken_huis_metpenup():
#     turtle.penup()
#     turtle.setpos(waarde, waarde)
#     turtle.pendown()
#     teken_huis(30)

for n in range(5):
    nieuw_punt_x = random.randint(-300,300)
    Xpunten.append(nieuw_punt_x)
    print(f"Nieuwe waarde 1 is {nieuw_punt_x}")
    
    print(Xpunten)


# for n in range(5):
#     nieuw_punt_x = random.randint(-300,300)
#     if nieuw_punt_x + 40 <= Xpunten[-1] and  nieuw_punt_x - 40 >= Xpunten[-1]:
#         print(f"Nieuwe waarde 1 is {nieuw_punt_x}")
#         Xpunten.append(nieuw_punt_x)
#     elif nieuw_punt_x + 40 <= Xpunten[-1] and  nieuw_punt_x - 40 >= Xpunten[-1]:
#         print(f"Nieuwe waarde 2 is {nieuw_punt_x}")
#         Xpunten.append(nieuw_punt_x)
#     elif nieuw_punt_x + 40 <= Xpunten[-1] and  nieuw_punt_x - 40 >= Xpunten[-1]:
#         print(f"Nieuwe waarde 3 is {nieuw_punt_x}")
#         Xpunten.append(nieuw_punt_x)    

    
    # nieuw_punt_y = random.randint(-300,300)
    
    # nieuw_punt_x = random.randint(-300,300)
    # nieuw_punt_y = random.randint(-300,300)
    # turtle.speed(30)
    # turtle.penup()
    # turtle.setpos(nieuw_punt_x, nieuw_punt_y)
    # turtle.pendown()
    # teken_huis(30)


# turtle.mainloop()