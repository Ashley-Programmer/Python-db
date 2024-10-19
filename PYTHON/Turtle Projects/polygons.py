import turtle

# create screen
screen = turtle.Screen()
screen.title("Polygons")
screen.bgcolor("black")

# create turtle
t = turtle.Turtle()
t.shape("turtle")
t.pencolor("white")
t.pensize(4)
t.speed(2)

t.penup()
t.goto(-50, 5)
t.pendown()


# function to draw a polygon, it loops through the num of sides
def draw_polygon(sides, size):
    # calculate each angle for each vertex
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.left(angle)


# draw a triangle with 3 sides 100 units
draw_polygon(3, 100)

# draw square (4 sides)
t.penup()
t.goto(-200, 0)
t.pendown()
draw_polygon(4, 100)

# draw pentagon 5 sides 100 units
t.penup()
t.goto(100, 0)
t.pendown()
draw_polygon(5, 100)

# draw square
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

screen.exitonclick()
