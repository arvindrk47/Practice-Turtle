import turtle

k=turtle.Turtle()
k.color("red","blue")
k.begin_fill()
k.speed(1)
k.forward(100)
k.left(90)
k.color("blue")
k.forward(100)
k.left(90)
k.forward(100)
k.color("red")
k.left(90)
k.forward(100)
k.end_fill()

k.penup()
k.forward(200)
k.pendown()

turtle.done()