import turtle

k = turtle.Turtle()
k.color("red","yellow")

k.begin_fill()
for i in range(10):
	k.forward(200)
	k.left(135)
k.end_fill()