# Desenho de circunferências com a biblioteca turtle
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.

import turtle

def circunferencia (cor, x,y,veloc,raio):
    for angle in range(0, 360, 15):
        turtle.goto( x ,y)
        turtle.color(cor)
        turtle.speed(veloc)
        turtle.seth(angle)
        turtle.circle(raio)

turtle.reset()
circunferencia("red",0,0,100,100)
circunferencia("black",-100,0,100,40)   
circunferencia("green",0,-100,100,40)
circunferencia("gray",100,0,100,40)
circunferencia("blue",0,100,100,40)
turtle.goto(-100,0)
turtle.done()