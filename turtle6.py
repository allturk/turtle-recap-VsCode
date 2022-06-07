import turtle as t

from random import randint

timmy=t.Turtle()
timmy.shape("blank")
t.colormode(255)
timmy.speed("fastest")
timmy.up()
timmy.goto(x=-100,y=100)
timmy.down()
def random_pen_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    randomColor=(r,g,b)
    return randomColor
angle=10

for _ in range(360//angle):
    timmy.right(angle)
    timmy.color(random_pen_color())
    timmy.circle(radius=70)

# ----------- or ---------------

timmy.up()
timmy.goto(x=100,y=-100)
timmy.down()

for _ in range(360//angle):
    timmy.color(random_pen_color())
    current_heading=timmy.heading()
    timmy.setheading(current_heading+angle)
    timmy.circle(radius=70)


screen=t.Screen()
screen.exitonclick()