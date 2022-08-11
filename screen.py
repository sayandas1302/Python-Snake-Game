def set_up_screen(screen):
    '''set up all the initial settings for the screen'''
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.title("The Snake Game")
    
def get_command(screen, snake):
    '''allows the screen to get command of the user regarding the movement of the snake'''
    screen.listen()
    screen.onkey(snake.go_up, "w")
    screen.onkey(snake.go_left, "a")
    screen.onkey(snake.go_down, "s")
    screen.onkey(snake.go_right, "d")