from turtle import Turtle

FONT = ("arial", 18, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        '''set all the initial settings of the scoreboard'''
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        '''shows the score at the top of the score board'''
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore}", align="center", font=FONT)
        
    def reset_score(self):
        '''reset the scoreboard with updation to the high scores'''
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode = "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.show_score()