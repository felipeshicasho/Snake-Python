from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
        self.refresh_position()

    def refresh_position(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
