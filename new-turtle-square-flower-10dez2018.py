import turtle

def desenhar_quadrado(tartaruga):
	for i in range(1,5):
		tartaruga.forward(100)
		tartaruga.right(90)

def desenhar():
	window = turtle.Screen()
	window.bgcolor("gray")

	joao = turtle.Turtle()
	joao.shape("turtle")
	joao.color("blue")
	joao.speed(10)

	for i in range(1,37):
		desenhar_quadrado(joao)
		joao.right(10)

	#maria = turtle.Turtle()
	#maria.shape("arrow")
	#maria.color("black")
	#maria.circle(100)

	window.exitonclick()

desenhar()

