from turtle import Turtle

class gameScreen:
    scores = [{"add": Turtle(), "score": 0, "pos": (-50,230)}, {"add": Turtle(), "score": 0, "pos": (50,230)}]
    writer = Turtle()

    def __init__(self):
        for i in range(2):
            scoreboard = self.scores[i]["add"]
            cScore = self.scores[i]["score"]
            position = self.scores[i]["pos"]
            scoreboard.color("white")
            scoreboard.hideturtle()
            scoreboard.penup()
            scoreboard.setposition(position)
            scoreboard.write(cScore,align="center",font=("Arial", 50, "bold"))
        self.centerLine()

    def centerLine(self):
        self.writer.setposition(0, -280)
        self.writer.speed(0)
        self.writer.shape("square")
        self.writer.hideturtle()
        self.writer.pencolor("white")
        self.writer.pensize(8)
        self.writer.setheading(90)
        stripes = 10
        move = 600/(stripes*2)
        for i in range(1, (stripes*2)+1):
            if i % 2 == 0:
                self.writer.penup()
                self.writer.forward(move)
            else:
                self.writer.pendown()
                self.writer.forward(move)

    def increaseScore(self, player):
        self.scores[player]["score"] = self.scores[player]["score"] + 1

    def returnScore(self, player):
        return self.scores[player]["score"]

    def updateScore(self):
        for i in range(2):
            scoreboard = self.scores[i]["add"]
            cScore = self.scores[i]["score"]
            scoreboard.clear()
            scoreboard.write(cScore,align="center",font=("Arial", 50, "bold"))