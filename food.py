from turtle import Turtle 
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.new_food()
        self.speed("fastest")
    
    #create random new food
    def new_food(self): 
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.random_x=random.randint(-280,280)
        self.random_y=random.randint(-280,280)
        self.goto(self.random_x,self.random_y)
    
     