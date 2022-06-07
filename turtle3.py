import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.pencolor("red")
timmy_the_turtle.pensize(2)

for _ in range(15):
    timmy_the_turtle.forward(5)
    timmy_the_turtle.up()
    timmy_the_turtle.forward(5)
    timmy_the_turtle.down()
  
screen=t.Screen()
screen.exitonclick()