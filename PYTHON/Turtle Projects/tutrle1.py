import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
t.speed(0)

colors = ['red', 'yellow']
for number in range(400):
    t.forward(number + 1)
    t.right(89)
    t.color(colors[number % 2])
turtle.done()
