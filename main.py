from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Tamanho da tela
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("JOGO DA COBRINHA")
screen.tracer(0)

# Classes com as suas funções
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

# Comandos pra andar
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Jogo ta rodando
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecta a colisão com a comidinha
    if snake.head.distance(food) < 15:
        food.refresh_position()
        snake.extend()
        scoreboard.increase()
    
    # Detecta a colisão com a parede
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detecta colisão com a própria cobra
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
