import turtle
import random
t = turtle.Turtle()
w =  turtle.Screen()
turtle.bgcolor('black')
t.pensize(4)
colors = ['green','red','blue','yellow','purple','pink','violet','orange']

def paralelogramo():
    for i in range(2):
        t.fd(100)
        t.rt(60)
        t.fd(100)
        t.rt(120)

for i in range(11):
    paralelogramo()
    t.rt(36)
    t.color(colors[i % 8])
turtle.done()    


