from turtle import Screen
import time
import random
from food import Food
from snake import Snake
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
food.relocate()
score = Score()


screen.listen()
screen.onkey(key="Up", fun=snake.move_north)
screen.onkey(key="Left", fun=snake.move_west)
screen.onkey(key="Right", fun=snake.move_east)
screen.onkey(key="Down", fun=snake.move_south)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        score.update_score()
        snake.grow()
        food.relocate()

    head = snake.turtles[0]
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for turtle in snake.turtles[1:]:
        if head.distance(turtle) < 5:
            game_is_on = False
            score.game_over()
screen.exitonclick()
