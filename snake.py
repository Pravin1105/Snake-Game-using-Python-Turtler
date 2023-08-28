import random
from turtle import Turtle
POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20

class Snake:
    def __init__(self):
        self.turtles = []
        self.create()

    def create(self):
        for pos in POS:
            self.add_seg(pos)

    def move(self):
        turtles = self.turtles
        turtles[0].speed("slow")
        for i in range(len(turtles) - 1, 0, -1):
            x = turtles[i - 1].xcor()
            y = turtles[i - 1].ycor()
            turtles[i].goto(x, y)
        turtles[0].forward(MOVE_FORWARD)

    def add_seg(self, pos):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.turtles.append(tim)

    def grow(self):
        self.add_seg(self.turtles[-1].position())

    def move_west(self):
        head = self.turtles[0].heading()
        if head != 0 and head != 180:
            self.turtles[0].seth(180)

    def move_north(self):
        head = self.turtles[0].heading()
        if head == 0 or head == 180:
            self.turtles[0].seth(90)

    def move_south(self):
        head = self.turtles[0].heading()
        if head == 0:
            self.turtles[0].seth(270)
        elif head == 180:
            self.turtles[0].seth(270)

    def move_east(self):
        head = self.turtles[0].heading()
        if head != 0 and head != 180:
            self.turtles[0].seth(0)

