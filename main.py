from turtle import Screen
from game import gameScreen
import time
from Paddle import paddle
from Ball import ball

def up1():
    p1.moveUp()
    screen.update()


def down1():
    p1.moveDown()
    screen.update()


def up2():
    p2.moveUp()
    screen.update()


def down2():
    p2.moveDown()
    screen.update()


screen = Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("black")
screen.listen()

screen.onkeypress(up1, "w")
screen.onkeypress(down1, "s")
screen.onkeypress(up2, "Up")
screen.onkeypress(down2, "Down")

screen.tracer(0)
gScreen = gameScreen()
p1 = paddle("left")
p2 = paddle("right")
pong = ball()
screen.update()
speed = 0.06
continue_game = True, None
while gScreen.returnScore(0) < 5 and gScreen.returnScore(1) < 5:
    while continue_game[0]:
        pong.checkHeading(p1.getLenArea(), p2.getLenArea())
        continue_game = pong.move()
        screen.update()
        time.sleep(speed)
    speed -= 0.01
    gScreen.increaseScore(continue_game[1])
    gScreen.updateScore()
    screen.update()
    time.sleep(2)
    pong.resetBall()
    p1.resetPaddle()
    p2.resetPaddle()
    screen.update()
    time.sleep(1)
    continue_game = True, None


screen.exitonclick()