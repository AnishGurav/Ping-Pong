from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING-PONG")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


ball.setheading(20)
x = 0.1
game_on = True
while game_on != False:
    time.sleep(x)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.setheading(360 - ball.heading())

    if ball.xcor() > 380:
        scoreboard.rwall_hit()
        scoreboard.update_score()
        ball.reset_ball()
        ball.setheading(ball.heading()+180)

    if ball.xcor() < -380:
        scoreboard.lwall_hit()
        scoreboard.update_score()
        ball.reset_ball()
        ball.setheading(ball.heading()+180)

    if r_paddle.distance(ball) < 50 and ball.xcor() > 320:
        ball.setheading(180 - ball.heading())
        scoreboard.add_rscore()
        scoreboard.update_score()
        if x != 0.03:
            x -= 0.01
        else:
            x = 0.03


    if l_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.setheading(180 - ball.heading())
        scoreboard.add_lscore()
        scoreboard.update_score()
        if x!=0.03:
            x -= 0.01
        else:
            x = 0.03


    if scoreboard.r_score > 9 or scoreboard.l_score>9:
        game_on = False
        scoreboard.game_over()








screen.exitonclick()
