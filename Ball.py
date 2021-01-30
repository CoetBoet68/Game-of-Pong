from turtle import Turtle

class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.setheading(45)

    def ballX(self):
        return self.pos()[0]

    def ballY(self):
        return self.pos()[1]

    def move(self):
        if 480 > self.ballX() > -480:
            self.forward(10)
            return True, None
        elif self.ballX() > 480:
            return False, 0
        else:
            return False, 1

    def resetBall(self):
        self.setposition(0,0)

    def checkHeading(self, minMax1,minMax2):
        checkMark = -440.0
        if self.ballX() >= abs(checkMark):
            if minMax2[0] > self.ballY() > minMax2[1]:
                if 360 > self.heading() >= 270:
                    self.setheading(self.heading() - 90)
                else:
                    self.setheading(self.heading() +  90)
        elif self.ballX() <= checkMark:
            if minMax1[0] > self.ballY() > minMax1[1]:
                if 180 > self.heading() >= 90:
                    self.setheading(self.heading() - 90)
                else:
                    self.setheading(self.heading() + 90)
        else:
            if self.ballY() <= -285:
                if 360 > self.heading() >= 270:
                    self.setheading(self.heading() - 270)
                else:
                    self.setheading(self.heading() - 90)
            elif self.ballY() >= 285:
                if 180 > self.heading() >= 90:
                    self.setheading(self.heading() +90)
                else:
                    self.setheading(self.heading() +270)
