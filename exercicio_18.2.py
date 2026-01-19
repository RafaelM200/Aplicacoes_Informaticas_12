import turtle
desenho= turtle.Turtle()
lado= int(input("Valor do lado:"))
for n in range(4):
    desenho.forward (lado)
    desenho.left (90)