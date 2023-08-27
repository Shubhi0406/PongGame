from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("MediumPurple")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def paddle1_miss(self):
        self.x_move = -10
        self.y_move = -10
        self.move_speed = 0.1

    def paddle2_miss(self):
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1