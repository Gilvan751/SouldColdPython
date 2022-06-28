from turtle import *
import turtle

painting = turtle.Turtle()

painting.pencolor("red")
painting.speed(0)


for x in range(60):
    painting.forward(60)
    painting.left(133)
painting.up()
painting.pencolor("blue")
painting.goto(100,100)
painting.pd()
for x in range(60):
    painting.forward(100)
    painting.left(153)
painting.up()
painting.pencolor("orange")
painting.goto(-50,100)
painting.pd()
for x in range(60):
    painting.forward(70)
    painting.left(153)
painting.up()
painting.pencolor("red")
painting.goto(-250,50)
painting.pd()
for x in range(60):
    painting.forward(90)
    painting.left(153)

turtle.done()
