import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

#turtle object creation
board = turtle.Turtle()

#creating a square
for i in range(12):
 board.forward(100)
 board.left(90)
 i = i+1