import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("green")

# Create a turtle to draw the heart
heart = turtle.Turtle()
heart.color("red")
heart.begin_fill()

# Drawing the heart shape
heart.left(50)
heart.forward(133)
heart.circle(50, 200)
heart.right(140)
heart.circle(50, 200)
heart.forward(133)

heart.end_fill()

# Hide the turtle and display the result
# heart.hideturtle()
# turtle.done()
screen.exitonclick()
