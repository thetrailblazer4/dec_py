import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def sqaure(length, angle):
	for i in range(4):
		my_turtle.forward(length)
		my_turtle.right(angle)


for i in range(200):
	sqaure(200,90)
	my_turtle.right(11)







turtle.done()