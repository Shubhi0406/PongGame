from turtle import Turtle

paddle_position = [(350, 0), (-350, 0)]
paddle_list = []


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.left(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        paddle_list.append(self)
        for paddle_num in range(len(paddle_list)):
            paddle_list[paddle_num].goto(paddle_position[paddle_num])

    def move_up(self):
        self.forward(50)

    def move_down(self):
        self.back(50)
