import turtle as turtle

from 04_turtle_functies import teken_veelhoek
from utils import usefull_functions.teken_parallelogram
from utils import usefull_functions.teken_veelhoek


def teken_kubus(lengte, hoek):
    teken_veelhoek(lengte, 4, "right")
    teken_parallelogram(lengte, lengte/2, hoek)
    turtle.goto(0,-lengte)
    teken_parallelogram(lengte, lengte/2, hoek)
    turtle.left(hoek)
    turtle.forward(lengte/2)
    turtle.right(hoek)
    teken_veelhoek(lengte, 4, "left")

teken_kubus(100, 40)

turtle.done()