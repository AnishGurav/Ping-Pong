from turtle import Turtle
# x = 45
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()


    def move(self):
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        # self.goto(new_x, new_y)
        self.forward(10)

    def reset_ball(self):
        self.goto(0,0)

    # def bounce_y(self):
    #     self.setheading(360-x)



