import turtle as turtle
turtle.shape(turtle)

def teken_driehoek(lengte):
    for x in range(3):
        turtle.forward(lengte)
        turtle.left(360/3)

def teken_vierhoek(lengte):
    for x in range(4):
        turtle.forward(lengte)
        turtle.right(360/4)

def teken_vijfhoek(lengte):
    for x in range(5):
        turtle.forward(lengte)
        turtle.right(360/5)

def teken_huis(lengte):
    teken_vierhoek(lengte = lengte)
    teken_driehoek(lengte)

def teken_cirkel(lengte, scherpte):
    for n in range(scherpte):
        turtle.forward(lengte)
        turtle.right(360/scherpte)

def parallelogram(degree, horizlength, sidelength):
    turtle.forward(horizlength)
    turtle.left(degree)
    turtle.forward(sidelength)
    turtle.left(180-degree)
    turtle.forward(horizlength)
    turtle.left(degree)
    turtle.forward(sidelength)
    turtle.left(180-degree)

def teken_parallelogram(degree, horizlength, sidelength):
    turtle.color('red')
    turtle.begin_fill() 
    for n in range(2):     
        turtle.forward(horizlength)
        turtle.left(degree)
        turtle.forward(sidelength)
        turtle.left(180-degree)
    turtle.end_fill()

def teken_trapezium(degree, length):
    turtle.forward(length)
    turtle.right(degree)
    turtle.forward(length)
    turtle.left(180-degree)
    turtle.forward(length/2)
    turtle.left(180-degree)
    turtle.forward(length)
    turtle.left(degree)

def teken_veelhoek(aantal_veelhoeken):
    for n in range(aantal_veelhoeken):
        turtle.forward(30)
        turtle.right(360/aantal_veelhoeken)

def teken_cijfer8(lengte, scherpte):
    for n in range(scherpte):
        turtle.forward(lengte)
        turtle.right(360/scherpte)
    turtle.left(90)
    for n in range(scherpte):
        turtle.forward(lengte)
        turtle.right(360/scherpte)

def teken_driehoek(lengte):
    for x in range(3):
        turtle.forward(lengte)
        turtle.left(360/3)

# Teken reflecterende driehoek zonder gebruik te maken van definities
def teken_reflecterende_driehoek(grootte):
    for x in range(3):
        turtle.forward(50)
        turtle.left(120)
    turtle.right(60)
    for x in range(3):
        turtle.forward(50)
        turtle.left(120)

def teken_reflecterende_driehoek_uit_def(lengte):
    teken_driehoek
    turtle.right(lengte)
    teken_driehoek

def teken_veelhoek_met_richting(lengte, hoeken, richting):
    if richting != "left" and richting != "right":
        print("Kies richting")
    else:
        for n in range (hoeken):
            if lengte == "left":
                turtle.forward(lengte)
                turtle.left(360/hoeken)
            if lengte == "right":
                turtle.forward(lengte)
                turtle.right(360/hoeken)

def teken_cubus(length):
    for n in range(4):
        turtle.forward(length)
        turtle.right(90)
    teken_parallelogram(325,length,length)



turtle.mainloop()

