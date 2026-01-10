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

def change_color():
    color = s.textinput("What color do you want?", "Color:")
    if color in colors:
        arrow.color(color)

def close_program():
    s.bye()



s = Screen()
change_color()
s.setup(700, 700)
s.listen()
s.onkey(close_program, "q")
s.onkey(fun=change_color, key="c")
s.onkey(fun=mv_forward, key="Up")
s.onkey(fun=mv_backward, key="Down")
s.onkey(fun=turn_left, key="Left")
s.onkey(fun=turn_right, key="Right")
s.onkey(fun=click_pen, key="space")
s.mainloop()