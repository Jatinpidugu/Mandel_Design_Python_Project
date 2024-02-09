import turtle
actor = turtle.Turtle()
window = turtle.Screen()

actor.pensize(3)
length = 200
actor.color('blue', 'blue')
actor.pensize(3)
increment = 30
colors = ["blue", "red", "green", "brown"]


def drawSquare(actor, x, y, length):
    actor.penup()
    actor.goto(x,y)
    actor.pendown()
    for n in range(4):
        actor.forward(length)
        actor.left(90)


for i in range(5):
    actor.color(colors[i])
    startx = -length //2
    starty = -length // 2
    length = length - increment
    startx = -length // 2
    starty = -length // 2
    drawSquare(actor,startx, starty, length)





