import turtle as t
from random import Random

ANGLES=[0,90,270,180]
t.colormode(255)
timmy=t.Turtle()
timmy.shape("blank")
timmy.pensize(5)
timmy.speed(6)
def random_color():
    r=Random().randint(0,255)
    g=Random().randint(0,255)
    b=Random().randint(0,255)
    randomColor= (r,g,b)
    return randomColor

for _ in range(150):
    timmy.right(Random().choice(ANGLES))
    # timmy.color(Random().choice(["red","blue","green","yellow","orange","purple","pink","brown","black"]))
    timmy.color(random_color())
    timmy.forward(20)
    

screen=t.Screen()
screen.exitonclick()
    

