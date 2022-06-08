from turtle import Turtle,Screen
import tkinter #To adding turtle screen window an icon
import time
from snake import Snake

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Create turtlescreen icon 
def createturtlescreenicon():
    img=tkinter.Image("photo",file="images/snake.png") #For adding  turtle screen window an icon
    screen._root.iconphoto(True,img) #For adding turtle screen window an icon


createturtlescreenicon()

screen.listen()
game_is_on=True

snake=Snake()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    head_position=snake.head.position()
    if head_position[0]>=295 or head_position[0]<=-295 or head_position[1]>=295 or head_position[1]<=-295:
        game_is_on=False
    screen.onkey(fun=snake.turn_left, key="Left")
    screen.onkey(fun=snake.go_up, key="Up")
    screen.onkey(fun=snake.go_down, key="Down")
    screen.onkey(fun=snake.turn_right, key="Right")














screen.exitonclick()