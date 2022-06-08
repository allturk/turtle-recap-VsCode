from turtle import Turtle, Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.direction="stop"
screen=Screen()

def timmy_move():
    timmy.forward(20)

#create a function timmy goes up
def timmy_go_up():
    if timmy.direction!="down":
        timmy.setheading(90)
   
#create a function timmy goes down
def timmy_go_down():
    if timmy.direction!="up":
        timmy.setheading(270)
#create a function timmy goes left
def timmy_go_left():
    if timmy.direction!="right":
        timmy.setheading(180)
#create a function timmy goes right
def timmy_go_right():
    if timmy.direction!="left":
        timmy.setheading(0)
screen.listen()
screen.onkey(timmy_go_up,"Up")
screen.onkey(timmy_go_down,"Down")
screen.onkey(timmy_go_left,"Left")
screen.onkey(timmy_go_right,"Right")
screen.onkey(timmy_move,"w")

screen.exitonclick()