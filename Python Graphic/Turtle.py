import turtle

# set s title for your canvas window
turtle.title("Richard's turtle")

# set up the screen size (in pixels - 425 x 425)
# set up starting point of the turtle (0,0)
turtle.setup(425,425,0,0)

NUM = int(input("Enter a number"))
A = 360/NUM
for i in range (NUM):
    turtle.forward(100)
    turtle.right(A)

turtle.goto(50,50)

turtle.exitonclick()

# turtle.penup()
# turtle.pendown()
