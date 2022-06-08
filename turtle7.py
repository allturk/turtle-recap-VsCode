import turtle as t 
from random import Random

timmy=t.Turtle()
timmy.shape("blank")
t.colormode(255)
timmy.speed("fastest")
timmy.up()
timmy.goto(x=-200,y=-200)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def random_pen_color():
    randomColor=Random().choice(color_list)
    return randomColor

def draw_dot():
    timmy.down()
    timmy.dot(20, random_pen_color())
    timmy.up()
    timmy.forward(50)
    

for _ in range(10):
    for _ in range(10):
        draw_dot()
    current_ycor=timmy.ycor()
    timmy.up()
    timmy.goto(x=-200, y=current_ycor+50)
    timmy.down()
screen=t.Screen()
screen.exitonclick()
