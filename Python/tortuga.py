import turtle as t
#fordward(), backwards(), right(), left(), home(), circle()
# color(), pendolork), bgcolor()
# penup(), pendown(), pensize(), speed()
# Piruleta
# Bucle
# Como usar una lista de colores
# ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime"]
t.title("Turtle Graphics . Portes Obertes")
t.pendown()
t.speed(0)
color = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime"]
t.bgcolor("black")
t.pensize(10)
t.pencolor("white")
t.pensize(100)
for j in range(360):
    t.pencolor(color[j % 10])

    for i in range(4):
        t.forward(100)
        t.left(90)

    t.left(1)

t.exitonclick()
