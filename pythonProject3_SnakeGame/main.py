from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
snake_score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detection collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake_score.increase_score()
        snake.update_snake()

    # detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        snake_score.game_over()
        
        
    #detect collision with tail
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on =False
            snake_score.game_over()

screen.exitonclick()
