"""set up turtle environment & import turtle module"""
import turtle

# set up screen
screen = turtle.Screen()
screen.title("Turtle Basics")
screen.bgcolor("green")

# create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

# move to a specific position # lift the pen not to draw anything
t.penup()
# move to the specified position(origin)
t.goto(0, 0)
# place the pen down to start drawing
t.pendown()

# draw a point # draw a dot with a diameter of 8 pixels with a red color
t.dot(8, "red")

"""draw a line from current position to another  move turtle forward by
100 units"""
t.forward(100)

# keep the window until clicked
screen.exitonclick()
