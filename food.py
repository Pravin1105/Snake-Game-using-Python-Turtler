import random
from turtle import Turtle
STRETCHED_WIDTH = 0.8
STRETCHED_LENGTH = 0.8
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=STRETCHED_WIDTH, stretch_len=STRETCHED_LENGTH)
        self.speed("fastest")

    def relocate(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

