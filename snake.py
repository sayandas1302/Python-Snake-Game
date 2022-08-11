from turtle import *

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake(Turtle):
    def __init__(self):
        '''creates all the initial settings for the snake'''
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''creates the snake by creating three different segments'''
        for position in STARTING_POSITION:
            self.add_segment(position)
        self.segments[0].color("red")

    def reset_snake(self):
        '''make the snake to reset to its initial position when the snake collides
           with wall or its tail'''
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        '''create a new segment of the snake body and add it to the main segments'''
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow_up(self):
        '''make the snake grow up by  adding a segment at the end of its body'''
        self.add_segment(self.segments[-1].pos())

    def move(self):
        '''make the snake move forward continuously'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(20)

    def go_up(self):
        '''if the snake head's direction is not down then it allow the snake head to go up'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        '''if the snake head's direction is not up then it allow the snake head to go down'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        '''if the snake head's direction is not left then it allow the snake head to go right'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def go_left(self):
        '''if the snake head's direction is not right then it allow the snake head to go left'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)