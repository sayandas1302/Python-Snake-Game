from turtle import *
from screen import *
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
# create the gaming screen
screen = Screen()
set_up_screen(screen)

# create the snake
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
is_game_on = True

# make the snake move
# create food
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # make the turn into direction
    get_command(screen, snake)

    # detect the collision to the food and do further proceeds
    if snake.head.distance(food) < 15:
        food.clear()
        food.relocate()
        scoreboard.score += 1
        scoreboard.show_score()
        snake.grow_up()
        
    # detect the collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    # detect the collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()