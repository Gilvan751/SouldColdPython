from turtle import *
import turtle
from random import randint

painting = turtle.Turtle()

painting.pencolor("red")
painting.speed(0)


def estrela():
    for i in range(60):
      
        painting.forward(90)
        painting.left(153)


def passo(color, goto):
    painting.up()
    painting.pencolor(color)
    painting.goto(goto)
    painting.pd()
        
passo('red',  (200,100))
estrela()

passo('blue', (150,100))
estrela()

passo('orange', (-50,100))
estrela()

passo('red', (-250,50))
estrela()

passo('green',(-250,-50))
estrela()

passo('green', (-100,-100))

estrela()


turtle.done()
