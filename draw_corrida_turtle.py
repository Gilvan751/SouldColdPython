import turtle
from turtle import*
from random import randint
speed(10)
up()


goto(-140,140)

for passo in range(15):
    write(passo, align='center')
    rt(90)
    fd(10)
    pd()
    fd(150)
    up()
    bk(160)
    lt(90)
    fd(20)


t1 = Turtle()
t1.color('red')
t1.shape('turtle')
t1.up()
t1.goto(-160, 100)
t1.pd

t2 = Turtle()
t2.color('blue')
t2.shape('turtle')
t2.up()
t2.goto(-160, 70)
t2.pd

t3 = Turtle()
t3.color('yellow')
t3.shape('turtle')
t3.up()
t3.goto(-160, 40)
t3.pd

t4 = Turtle()
t4.color('orange')
t4.shape('turtle')
t4.up()
t4.goto(-160, 10)
t4.pd

t5 = Turtle()
t5.color('violet')
t5.shape('turtle')
t5.up()
t5.goto(-160, -20)
t5.pd

for turn in range(100):
    t1.fd(randint(1,5))
    t2.fd(randint(1,5))
    t3.fd(randint(1,5))
    t4.fd(randint(1,5))
    t5.fd(randint(1,5))


turtle.done()


