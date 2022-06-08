from turtle import Turtle, Screen
XCOR=[0,-20,-40]
#create Snake class


class Snake:
    def __init__(self):
        self.snakes=[]
        self.create_snake()
        self.head=self.snakes[0]
       
    
    def create_snake(self):
        for _ in range(3):
            self.create_snakesegments(XCOR[_])

    def create_snakesegments(self, xcor):
        body=Turtle()
        body.speed(0)
        body.shape("square")
        body.color("white")
        body.penup()
        body.goto(xcor,0)
        body.direction="stop"
        self.snakes.append(body)

    def move(self):
        for seg_num in range(len(self.snakes)-1,0,-1):
            x=self.snakes[seg_num-1].xcor()
            y=self.snakes[seg_num-1].ycor()
            self.snakes[seg_num].goto(x,y)
        self.snakes[0].forward(20)
            
    def turn_left(self):
        if self.snakes[0].direction!="right":
            self.snakes[0].left(90)
    def turn_right(self):
        if self.snakes[0].direction!="left":
            self.snakes[0].right(90)
    def go_up(self):
        if self.snakes[0].direction!="down":
            self.snakes[0].setheading(90)
    def go_down(self):
        if self.snakes[0].direction!="up":
            self.snakes[0].setheading(270)


    