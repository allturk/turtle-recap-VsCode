from turtle import Turtle, Screen
XCOR=[0,-20,-40]
#create Snake class


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snakes=[]
        
        self.create_snake(XCOR)
      
        self.head=self.snakes[0]
       
    
    def create_snake(self,x):
        
        for pos in x:
            self.create_snakesegment()
            self.new_segment.goto(pos,0)
            self.snakes.append(self.new_segment)

    #create snake segment
    def create_snakesegment(self):
        self.new_segment=Turtle()
        self.new_segment.direction="go"
        self.new_segment.speed(0)
        self.new_segment.shape("square")
        self.new_segment.color("white")
        self.new_segment.penup()
        
        
        
        
        
    def add_segment(self):
        x_cor=self.snakes[-1].xcor()
        y_cor=self.snakes[-1].ycor()
        # print(x_cor," ",y_cor)
        self.create_snakesegment()
        self.new_segment.goto(x_cor,y_cor)
        self.snakes.append(self.new_segment)
        

    def move(self):
        for seg_num in range(len(self.snakes)-1,0,-1):
            x=self.snakes[seg_num-1].xcor()
            y=self.snakes[seg_num-1].ycor()
            self.snakes[seg_num].goto(x,y)
        self.head.forward(20)
            
    def find_distance(self,element):
        head_distance=self.head.distance(element)
        return head_distance

    def go_left(self):
        if self.head.direction!="right":
            self.head.setheading(180)
    def go_right(self):
        if self.head.direction!="left":
            self.head.setheading(0)
    def go_up(self):
        if self.head.direction!="down":
            self.head.setheading(90)
    def go_down(self):
        if self.head.direction!="up":
            self.head.setheading(270)


    