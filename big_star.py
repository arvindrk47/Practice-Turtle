import turtle

k=turtle.Turtle()
k.color("red","yellow")
k.speed(10)

k.begin_fill()
for i in range(100):
	k.forward(200)
	k.left(168.5)
k.end_fill()