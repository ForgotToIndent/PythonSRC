import turtle

wn = turtle.Screen()
wn.setup(width="1000", height="1000")
wn.bgcolor("lightgreen")

exturtle = turtle.Turtle()

exturtle.shape("turtle")
exturtle.color("blue")

exturtle.forward(100)
exturtle.right(90)
exturtle.forward(50)

wn.exitonclick()