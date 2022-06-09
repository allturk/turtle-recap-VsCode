from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.color("blue")
        self.goto(x=-30,y=270)
        self.write("Score: {}".format(self.score),align="center",font=("Courier",20,"normal"))

    def update_score(self,score):
        self.score=score
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Courier",20,"normal"))
        