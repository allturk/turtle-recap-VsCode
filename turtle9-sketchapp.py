from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()
screen.listen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counterclockwise():
    current_heading=tim.heading()
    tim.setheading(current_heading-10)
    # tim.forward(distance=5)


def move_clockwise():
    current_heading=tim.heading()
    tim.setheading(current_heading+10)
    # tim.forward(distance=5)

def clear_screen():
    screen.reset()

screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_counterclockwise, key="a")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=clear_screen, key="c")


screen.exitonclick()









