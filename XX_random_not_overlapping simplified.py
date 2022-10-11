import turtle as turtle
from random import randint
import time
from utils.usefull_functions import teken_huis

list_Xcoordinates = [10]
# list_Ycoordinates = []

new_Xcoor = 0
# new_ycoor = 0

for i in range(2):
    new_Xcoor = randint(1, 13)
    # This while-loop will determine of the created Xcoor will overlap the last used Xcoor
    while 10 > new_Xcoor:
        new_Xcoor = randint(1, 13)
        print(f"The generated Xcoor {new_Xcoor} is smaller then the list Xcoor {list_Xcoordinates[-1]}.")
        if list_Xcoordinates[-1] < new_Xcoor:
            time.sleep(3)
            print(f"The generated Xcoor {new_Xcoor} is bigger then the list Xcoor {list_Xcoordinates[-1]}.")







teken_huis(75)


turtle.mainloop()