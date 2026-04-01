import turtle as t
#fordward(), backwards(), right(), left(), home(), circle()
# color(), pendolork), bgcolor()
# penup(), pendown(), pensize(), speed()
# Piruleta
# Bucle
# Como usar una lista de colores
# ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime"]
# t.title("Turtle Graphics . Portes Obertes")
# t.pendown()
# t.speed(0)
# color = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime"]
# t.bgcolor("black")
# t.pensize(10)
# t.pencolor("white")
# t.pensize(100)
# for j in range(360):
#     t.pencolor(color[j % 10])
#
#     for i in range(4):
#         t.forward(100)
#         t.left(90)
#
#     t.left(1)
#
# t.exitonclick()
def arbre(nivell, mida):
    if nivell == 1:
        t.forward(mida)
        t.forward(-mida)
    else:
        t.forward(mida)
        t.right(-45)
        arbre(nivell - 1, mida)
        t.right(90)
        arbre(nivell - 1, mida)
        t.right(-45)
        t.backward(mida)
def main():
    nivell = 3
    if nivell == 0:
        return
    t.left(90)
    arbre(nivell, 100)
    t.exitonclick()

if __name__ == "__main__":
    main()