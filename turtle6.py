import turtle as t

from random import randint

timmy=t.Turtle()
timmy.shape("blank")
t.colormode(255)
timmy.speed("fastest")
timmy.up()
timmy.goto(x=-100,y=100)
timmy.down()
def move_turtle(x,y):
    timmy.up()
    timmy.goto(x,y)
    timmy.down()
def random_pen_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    randomColor=(r,g,b)
    return randomColor
angle=10

def draw_spirograph(angle):
    for _ in range(360//angle):
        timmy.right(angle)
        timmy.color(random_pen_color())
        timmy.circle(radius=70)

move_turtle(-100, 100)
draw_spirograph(angle)

# ----------- or ---------------

move_turtle(100, -100)

draw_spirograph(angle)


screen=t.Screen()
screen.exitonclick()