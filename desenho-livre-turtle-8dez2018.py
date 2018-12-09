import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("lightblue")

	joao = turtle.Turtle()
	joao.shape("turtle")
	joao.color("black")
	joao.speed(6)

	joao.forward(1000)
	joao.forward(-1000)

	joao.right(200)

	joao.forward(100)
	joao.left(200)

	joao.forward(100)
	joao.left(60)

	joao.forward(100)
	joao.right(120)

	joao.forward(100)
	joao.left(60)

	joao.forward(100)
	joao.left(200)

	joao.forward(100)
	joao.right(200)

	joao.forward(1000)
	joao.forward(-1000)

	joao.right(800)
	joao.forward(100)

	window.exitonclick()

draw_square()