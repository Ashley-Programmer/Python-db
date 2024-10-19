import turtle

screen = turtle.Screen()
screen.bgcolor("black")
win = turtle.Turtle()
win.color("red")
# win.shape("turtle")
win.pensize(2)
win.speed(1000)

def spiral():
    for x in range(36):
        win.forward(5)
        win.left(3)
    for x in range(18):
        win.forward(10)
        win.right(3)
    win.right(180)
    for y in range(18):
        win.forward(10)
        win.left(3)
    for y in range(36):
        win.forward(5)
        win.right(3)
    win.right(180)
    win.left(9)

win.begin_fill()
for i in range(40):
    spiral()
win.fillcolor("black")
win.end_fill()

# turtle.done()
screen.exitonclick()