import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("purple")

	joao = turtle.Turtle()
	joao.shape("circle")
	joao.color("grey")
	joao.speed(10)

	joao.forward(100)
	joao.right(120)

	joao.forward(100)
	joao.right(60)

	joao.forward(100)
	joao.right(60)

	joao.forward(100)
	joao.right(120)

	joao.forward(100)
	joao.right(120)

	## primeira etapa - quadrado

	joao2 = turtle.Turtle()
	joao2.shape("arrow")
	joao2.color("black")
	joao2.speed(10)

	joao2.forward(120)
	joao2.right(90)

	joao2.forward(120)
	joao2.right(90)

	joao2.forward(120)
	joao2.right(90)

	joao2.forward(120)
	joao2.right(90)


	joao3 = turtle.Turtle()
	joao3.shape("arrow")
	joao3.color("black")
	joao3.speed(6)

	joao3.forward(200)
	joao3.right(90)

	joao3.forward(200)
	joao3.right(90)

	joao3.forward(200)
	joao3.right(90)

	joao3.forward(200)
	joao3.right(90)


	joao4 = turtle.Turtle()
	joao4.shape("arrow")
	joao4.color("black")
	joao4.speed(4)

	joao4.forward(300)
	joao4.right(90)

	joao4.forward(300)
	joao4.right(90)

	joao4.forward(300)
	joao4.right(90)

	joao4.forward(300)
	joao4.right(90)

	## segunda etapa - quadrado

	joao5 = turtle.Turtle()
	joao5.shape("arrow")
	joao5.color("white")
	joao5.speed(10)

	joao5.forward(120)
	joao5.left(90)

	joao5.forward(120)
	joao5.left(90)

	joao5.forward(120)
	joao5.left(90)

	joao5.forward(120)
	joao5.left(90)


	joao6 = turtle.Turtle()
	joao6.shape("arrow")
	joao6.color("white")
	joao6.speed(10)

	joao6.forward(200)
	joao6.left(90)

	joao6.forward(200)
	joao6.left(90)

	joao6.forward(200)
	joao6.left(90)

	joao6.forward(200)
	joao6.left(90)

	joao7 = turtle.Turtle()
	joao7.shape("arrow")
	joao7.color("white")
	joao7.speed(10)

	joao7.forward(300)
	joao7.left(90)

	joao7.forward(300)
	joao7.left(90)

	joao7.forward(300)
	joao7.left(90)

	joao7.forward(300)
	joao7.left(90)


	window.exitonclick()

draw_square()