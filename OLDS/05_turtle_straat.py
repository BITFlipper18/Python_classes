import turtle as turtle
from utils.usefull_functions import teken_huis


coordinaten = []

coordinaten.append((0,0))
# coordinaten.append("a")
# coordinaten.append("b")
# coordinaten.append("a")

print(coordinaten)
# coordinaten.append("a", "b")

coordinaten.append((100, 100))

print(coordinaten)
# laatste = coordinaten.pop()
# print(laatste)

print(coordinaten)


print(type("a"))
print(type((0,0)))
print(type(5))

print(coordinaten[0])

for x in range(len(coordinaten)):
    print(coordinaten[x])

for coor in coordinaten:
    print(coor)

def teken_driehoek(lengte):
    for x in range(3):
        turtle.forward(lengte)
        turtle.left(360/3)

def teken_vierhoek(lengte):
    for x in range(4):
        turtle.forward(lengte)
        turtle.right(360/4)



aantal_huizen = 2

for i in range(aantal_huizen):
    teken_driehoek(50)










# for data in list:
#     try:
#         int(data)
