from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 60, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 60, "normal"))

    def add_rscore(self):
        self.r_score += 1
        self.clear()

    def add_lscore(self):
        self.l_score += 1
        self.clear()

    def lwall_hit(self):
        self.r_score += 1
        self.clear()

    def rwall_hit(self):
        self.l_score += 1
        self.clear()


    def game_over(self):
        if self.r_score == 10:
            self.goto(0, 0)
            self.write(f"GAME OVER!\nThe winner is RIGHT", align="center", font=("Arial", 30, "normal"))
        elif self.l_score == 10:
            self.goto(0, 0)
            self.write(f"GAME OVER!\nThe winner is LEFT", align="center", font=("Arial", 30, "normal"))

