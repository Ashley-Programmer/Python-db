import turtle

win = turtle.Screen()
win.title("Draw")
win.bgcolor("black")

x = turtle.Turtle()
x.shape("turtle")
x.pencolor("red")
x.speed(8)

for outerLoop in range(18):
    x.pensize(3)
    x.forward(100)
    x.right(90)
    x.forward(100)
    x.right(90)
    x.forward(100)
    x.right(90)
    x.forward(100)
    x.right(90)
    x.right(20)
for innerLoop in range(1):
    x.pencolor("yellow")
    x.pensize(3)
    x.circle(100)
    x.circle(85)
    x.circle(70)
    x.circle(50)
for innerLoop in range(1):
    x.pencolor("yellow")
    x.pensize(3)
    x.circle(-100)
    x.circle(-85)
    x.circle(-70)
    x.circle(-50)
# to the sides
side_Circles = [(-150, 0), (150, 0)]
for sidesPosition in side_Circles:
    # x.penup()
    # x.goto(sidesPosition[0], sidesPosition[1])
    # x.pendown()
    # for sideLoop in range(1):
    x.goto(0, 0)
    x.setheading(x.towards(0, -8))
    x.pencolor("aqua")
    x.pensize(3)
    x.circle(100)
    x.circle(85)
    x.circle(70)
    x.circle(50)
for sidesPosition in side_Circles:
    x.goto(0, 0)
    x.setheading(x.towards(1, -8))
    x.pencolor("aqua")
    x.pensize(3)
    x.circle(-100)
    x.circle(-85)
    x.circle(-70)
    x.circle(-50)

win.exitonclick()
