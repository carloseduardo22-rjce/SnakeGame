from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Placar

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da cobra")
# Esta função é usada para ativar ou desativar a
# animação da tartaruga e definir
# um atraso para atualizar os desenhos.
screen.tracer(0)

snake = Snake()
food = Food()
placar = Placar()

#método para ouvir meu teclado
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detectar a colisão de alimentos
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        placar.aumentarplacar()

    # Detectar colisão com a parede
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game_is_on = False
        placar.game_over()

    # Detectar colisão com a cauda
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            placar.game_over()



screen.exitonclick()



