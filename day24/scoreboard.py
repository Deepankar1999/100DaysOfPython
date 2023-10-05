from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
DATAFILE="/Users/2178053/100dayspython/100DaysOfPython/day24/d24snakegamedata.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=self.fetch_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def fetch_score(self):
        with open(DATAFILE) as file:
            return int(file.read())
    def write_score(self):
        with open(DATAFILE,mode="w") as file:
            file.write(f"{self.score}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        self.score=0
        self.update_scoreboard() 
    
    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        self.write_score()
