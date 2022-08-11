from random import *
from turtle import *

class Food(Turtle):
    def __init__(self):
        '''creates the food and initially set it at a random point on the game screen'''
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.turtlesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.penup()
        self.relocate()

    def relocate(self):
        '''set the food to a radomly selected point on the game screen'''
        x_pos = randint(-280, 280)
        y_pos = randint(-280, 280)
        self.goto(x_pos, y_pos)