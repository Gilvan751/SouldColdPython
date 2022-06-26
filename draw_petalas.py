
from turtle import *
import turtle as tur


def petal1(t1, r, ang):
    for i in range(2):
        t1.circle(r, ang)
        t1.left(180 - ang)


def flower1(t1, n, r, ang):
    for i in range(n):
        petal1(t1, r, ang)
        t1.left(360.0 / n)


def move(t1, len):
    win = tur.Screen()
    win.bgcolor("cyan")
    t1.pu()
    t1.fd(len)
    t1.pd()


ws = tur.Turtle()
ws.speed(100)

ws.color("pink")
ws.shape("turtle")
move(ws, -150)
ws.begin_fill()
flower1(ws, 7, 50.0, 50.0)
ws.end_fill()

ws.color("blue")
move(ws, 150)
ws.begin_fill()
flower1(ws, 9, 20.0, 60.0)
ws.end_fill()

ws.color("green")
move(ws, 150)
ws.begin_fill()
flower1(ws, 13, 60.0, 40.0)
ws.end_fill()

ws.color('yellow')
move(ws, -400)
flower1(ws, 8, 70, 100)
ws.end_fill()

tur.mainloop()
