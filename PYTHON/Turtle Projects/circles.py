import turtle

# create scree
window = turtle.Screen()
window.title("Circles & Ellipses")
window.bgcolor("black")

# create turtle
circle = turtle.Turtle()
circle.shape("turtle")
circle.pencolor("white")
circle.pensize(4)
circle.speed(4)

# draw the circle with 100 units radius
circle.circle(100)

window.exitonclick()
