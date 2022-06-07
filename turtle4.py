import turtle as t 
from random import Random
timmy=t.Turtle()
timmy.shape("turtle")
flag=True
sides=3
while flag:
    for n in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)
    timmy.color(Random().choice(["red","blue","green","yellow","orange","purple","pink","brown","black"]))
    sides+=1
    if sides>10:
        flag=False
t.Screen().exitonclick()