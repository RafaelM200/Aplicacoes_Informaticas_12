# Desenho de um quadrado usando a biblioteca turtle
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.

import turtle
desenho= turtle.Turtle()
lado= int(input("Valor do lado:"))

for n in range(4):
    desenho.forward (lado)
    desenho.left (90)

turtle.done()