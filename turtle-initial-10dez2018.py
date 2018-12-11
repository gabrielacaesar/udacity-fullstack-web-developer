import turtle

def desenhar_iniciais():
	window = turtle.Screen()
	window.bgcolor("purple")
	window.title("writing my initials")

	letter_g = turtle.Turtle()
	letter_g.shape("arrow")
	letter_g.color("black")
	letter_g.speed(1)

	letter_g.write('Udacity - Fullstack', True,'center',('Helvetica', 10, 'bold'))

	letter_g.left(90)
	letter_g.forward(100)
	letter_g.left(450)
	letter_g.forward(100)
	letter_g.back(100)
	letter_g.left(90)
	letter_g.forward(100)
	letter_g.right(90)
	letter_g.forward(100)
	letter_g.right(45)
	letter_g.forward(150)
	letter_g.right(45)
	letter_g.forward(100)
	letter_g.right(45)
	letter_g.forward(100)
	letter_g.right(45)
	letter_g.forward(125)
	letter_g.penup()
	letter_g.forward(50)


desenhar_iniciais()



