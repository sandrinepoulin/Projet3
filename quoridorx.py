import turtle

'''interface graphique du jeu'''

fen = turtle.Screen()
fen.title("Jeu Quoridor")
fen.setup(width=750, height=750)

tim = turtle.Turtle()
tim.shape('turtle')
tim.speed('fastest')
tim.color('saddlebrown')
tim.pensize(2)

#carré extérieur
tim.penup()
tim.backward(300)
tim.right(90)
tim.forward(300)
tim.pendown()
for i in range(4):
    tim.left(90)
    tim.forward(603)

#lignes horozontales
tim.penup()
tim.backward(67)
tim.left(90)
for i in range(8):
    tim.pendown()
    tim.forward(603)
    tim.penup()
    tim.left(90)
    tim.forward(67)
    tim.right(90)
    tim.backward(603)
    tim.pendown()

#lignes verticales
tim.penup()
tim.forward(67)
tim.right(90)
for i in range(8):
    tim.pendown()
    tim.forward(603)
    tim.penup()
    tim.left(90)
    tim.forward(67)
    tim.right(90)
    tim.backward(603)

#numéros: 9
tim.penup()
tim.right(90)
tim.forward(640)
tim.left(90)
tim.forward(30)
tim.pendown()
tim.circle(10)
tim.left(90)
tim.penup()
tim.forward(20)
tim.pendown()
tim.right(90)
tim.forward(20)

#8
tim.left(90)
tim.penup()
tim.backward(20)
tim.right(90)

tim.forward(40)
tim.pendown()
tim.circle(10)
tim.penup()
tim.forward(20)
tim.pendown()
tim.circle(10)

#7
tim.penup()
tim.forward(40)
tim.pendown()
tim.left(90)
tim.forward(20)
tim.right(110)
tim.forward(40)

#6
tim.penup()
tim.left(20)
tim.forward(30)
tim.pendown()
tim.right(20)
tim.forward(30)
tim.left(20)
tim.circle(10)

#5
tim.penup()
tim.forward(35)
tim.left(90)
tim.forward(25)
tim.pendown()
tim.backward(20)
tim.right(90)
tim.forward(20)
tim.left(90)
tim.forward(10)
for i in range(20):
    tim.right(9)
    tim.forward(2)
tim.forward(10)

#4
tim.penup()
tim.left(90)
tim.forward(25)
tim.pendown()
tim.forward(20)
tim.left(90)
tim.forward(20)
tim.right(90)
tim.backward(20)
tim.forward(40)

#3
tim.penup()
tim.forward(25)
tim.right(90)
tim.forward(20)
tim.pendown()
tim.backward(20)
tim.left(45)
tim.forward(20)
tim.right(45)
tim.backward(5)
for i in range(25):
    tim.right(9)
    tim.backward(2)

#2
tim.penup()
tim.right(45)
tim.forward(35)
tim.pendown()
for i in range(22):
    tim.right(10)
    tim.backward(2)
tim.backward(30)
tim.right(50)
tim.forward(25)

#1
tim.penup()
tim.right(110)
tim.forward(35)
tim.left(20)
tim.pendown()
tim.forward(40)


turtle.mainloop()