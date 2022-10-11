import turtle as turtle
from random import randint
import time
from utils.usefull_functions import teken_huis

list_Xcoordinates = [0, 0]
# list_Ycoordinates = []

new_Xcoor = 0
# new_ycoor = 0

for i in range(2):
    time.sleep(2)
    new_Xcoor = randint(-15, 15)
    print(f"List coor is {list_Xcoordinates[-1]}")
    time.sleep(1)
    print(f"Generated Xcoor : {new_Xcoor}")
    # This while-loop will determine of the created Xcoor will overlap the last used Xcoor
    while list_Xcoordinates[-1] > new_Xcoor -10 and list_Xcoordinates[-1] < new_Xcoor +10:
        time.sleep(2)
        print(f"WRONG The generated Xcoor {new_Xcoor} WILL overlap last value {list_Xcoordinates[-1]}.")
        if list_Xcoordinates[-1] > new_Xcoor +1:
            time.sleep(3)
            print(f"CORRECT The generated Xcoor {new_Xcoor} will NOT overlap last value {list_Xcoordinates[-1]}.")







teken_huis(75)


turtle.mainloop()