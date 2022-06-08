from turtle import Screen
import tkinter #To adding turtle screen window an icon
import time
from snake import Snake
from food import Food

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
snake_food=Food()
print("random_x", snake_food.random_x)


def find_distance():
    head_distance=snake.head.distance(snake_food)
    return head_distance


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    head_position=snake.head.position()
    if head_position[0]>=295 or head_position[0]<=-295 or head_position[1]>=295 or head_position[1]<=-295:
        game_is_on=False
    if find_distance()<=15:
        snake_food.reset()
        snake_food.new_food()
        snake.add_segment()
   
    screen.onkey(fun=snake.go_left, key="Left")
    screen.onkey(fun=snake.go_up, key="Up")
    screen.onkey(fun=snake.go_down, key="Down")
    screen.onkey(fun=snake.go_right, key="Right")














screen.exitonclick()