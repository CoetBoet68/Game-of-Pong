from turtle import Turtle


class paddle(Turtle):
    side = ""
    posi = (0, 0)

    def __init__(self, side):
        super().__init__()
        self.side = side
        if self.side == "left":
            self.posi = (-460, 0)
        else:
            self.posi = (460, 0)
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=6.5, stretch_wid=0.8)
        self.setposition(self.posi)
        self.setheading(90)

    def moveUp(self):
        if self.getY() < 230:
            self.forward(45)

    def moveDown(self):
        if self.getY() > -230:
            self.backward(45)

    def getY(self):
        return self.pos()[1]

    def getLenArea(self):
        max = self.getY() + 80
        min = self.getY() - 80
        return max, min

    def resetPaddle(self):
        self.setposition(self.posi)