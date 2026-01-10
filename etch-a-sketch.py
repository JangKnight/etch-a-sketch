from turtle import *

arrow = Turtle(shape="arrow")
colors = ["red", "blue", "green", "black", "purple", "orange", "pink", "brown", "yellow"]
mode("logo")
arrow.penup()
pen = False

def mv_forward():
    arrow.forward(10)

def mv_backward():
    arrow.backward(10)

def turn_left():
    arrow.left(10)

def turn_right():
    arrow.right(10)

def click_pen():
    global pen
    if pen:
        arrow.penup()
        pen = False
    else:
        arrow.pendown()
        pen = True



s = Screen()
s.setup(700, 700)
s.listen()
turtle_color = s.textinput("What color do you want?", "Color:")
if turtle_color in colors:
    arrow.color(turtle_color)
s.onkey(mv_forward, "Up")
s.onkey(mv_backward, "Down")
s.onkey(turn_left, "Left")
s.onkey(turn_right, "Right")
s.onkey(click_pen, "space")
s.exitonclick()