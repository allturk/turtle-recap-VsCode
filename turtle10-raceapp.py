from turtle import Turtle, Screen
from random import Random
#create a color list from rainbow colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']



screen=Screen()
screen.setup(width=500,height=400)
is_race_on=False
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
turtles=[]
def create_turtles():
    global turtles
    ycor_plus=40
    current_cor=-100
    for _ in range(6):
        turtles.append(Turtle(shape="turtle"))
        print(len(turtles))
        color=Random().choice(colors)
        colors.pop(colors.index(color))
        turtles[_].color(color)
        turtles[_].penup()
        # turtles[_].goto(-230,(_*-30)+100)
        turtles[_].goto(-230,current_cor)
        current_cor+=ycor_plus
create_turtles()
print(len(turtles))
if user_bet:
    is_race_on=True

while is_race_on:
    moving_dist=Random().randint(0, 10)
    indeks=Random().randint(0, len(turtles)-1)
    turtles[indeks].forward(moving_dist)
    x_cor=turtles[indeks].xcor()
    if x_cor>=240:
        is_race_on=False
        turtle_color=turtles[indeks].color()
        if turtle_color[0]==user_bet:
            print(f"{turtle_color[0]} win the race. You WIN the BET")
        else:
            print(f"{turtle_color[0]} win the race.  You lost!")

#or
# while is_race_on:
    
#     for turtle in turtles:
#         moving_dist=Random().randint(0, 10)
#         x_cor=turtle.xcor()
#         turtle.forward(moving_dist)
#         if x_cor>=232:
#             is_race_on=False
#             turtle_color=turtle.pencolor()
#             if turtle_color[0]==user_bet:
#                 print(f"{turtle_color} turtle win the race. You WIN the BET")
#             else:
#                 print(f"{turtle_color} turtle win the race.  You lost!")
# # tim.shape("turtle")

screen.exitonclick()