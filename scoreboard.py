from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier",20,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.color("blue")
        self.goto(x=-30,y=270)
        self.write("Score: {}".format(self.score),align=ALIGNMENT,font=FONT)

    def update_score(self,score):
        self.score=score
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        
    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)