from turtle import Turtle
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_Score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"score: {self.score}", align="center", font = FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_Score}", align="center", font = FONT)


    def reset(self):
        if self.score > self.high_Score:
            self.high_Score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.high_Score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=FONT)