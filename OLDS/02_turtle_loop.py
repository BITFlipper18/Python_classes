import turtle as turtle

# turtle.done()

turtle.title("Moving turtle")

# Make turtle walk a rectangle
# turtle.shape("turtle")
# turtle.fillcolor("orange")
# turtle.forward(300)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(300)
# turtle.right(90)
# turtle.forward(200)

# Make turtle walk a triangle
# corners = input("How many corners do you want")

turtle.shape("turtle")
turtle.fillcolor("purple")

for n in range(7):
    turtle.forward(150)
    turtle.right(360/7)

turtle.mainloop()