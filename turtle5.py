import turtle as t
from random import Random

ANGLES=[0,90,270,180]

timmy=t.Turtle()
timmy.shape("blank")
timmy.pensize(5)
timmy.speed(6)

for _ in range(150):
    timmy.right(Random().choice(ANGLES))
    timmy.color(Random().choice(["red","blue","green","yellow","orange","purple","pink","brown","black"]))
    timmy.forward(20)
    

screen=t.Screen()
screen.exitonclick()
    

