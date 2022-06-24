import turtle
t = turtle.Turtle()
w = turtle.Screen()
total = 0
t.pensize(4)
colors = ['purple','red','blue','violet','orange','cyan']
def quadrado(t):
    for i in range(4):
        t.fd(100)
        t.rt(90)
def circulo(t):
    for i in range(18):
        t.fd(20)
        t.rt(20)

def spiral(t):
    for i in range(18):
        t.color(colors[i % 6])
        quadrado(t)
        t.rt(20)



spiral(t)
turtle.done()