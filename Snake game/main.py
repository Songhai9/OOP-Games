from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def quit_game():
    global game_is_on
    game_is_on = False


# Screen config
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# Scoreboard
scoreboard = Scoreboard()


# Snake creation and key binding
snake = Snake()
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=quit_game, key="q")


# Food initialization
food = Food()

# Visualization
screen.update()

# Main loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food + managing score and grotwth
    if snake.head.distance(food) < 15:
        snake.grow()
        food.refresh()
        scoreboard.score += 1
        scoreboard.update_score()

    # Detect collision with walls
    if (
        (snake.head.xcor() > 290)
        or (snake.head.xcor() < -290)
        or (snake.head.ycor() > 290)
        or (snake.head.ycor() < -290)
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for block in snake.snake_body[1:]:
        if snake.head.distance(block) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
