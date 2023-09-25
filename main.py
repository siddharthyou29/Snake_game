from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Sid\'s Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.score_update()

    pos_x = snake.head.xcor()
    pos_y = snake.head.ycor()

    if pos_x > 300:
        snake.head.goto(-300, pos_y)
    elif pos_x < -300:
        snake.head.goto(300, pos_y)
    elif pos_y > 300:
        snake.head.goto(pos_x, -300)
    elif pos_y < -300:
        snake.head.goto(pos_x, 300)

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()