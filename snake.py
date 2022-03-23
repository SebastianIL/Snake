"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
import random
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Con ayuda del import random se generarn colores diferentes, tanto para el snake como para food
hexas= ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
hexaf= ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        #Se inserta el color al azar para snake
        square(body.x, body.y, 9, hexas)

   #Se inserta el color al azar para food
    square(food.x, food.y, 9, hexaf)
    update()
    ontimer(move, 100)


def movefood():
    #Se mueve la comida sin salir del cuadro
    food.x =+ randrange(-10, 11, 10)
    food.y =+ randrange(-10, 11, 10)

    #Detectar si sigue dentro del cuadro
    if not inside(food):
        food.x = randrange(-15, 15) * 20
        food.y = randrange(-15, 15) * 20

    ontimer(movefood, 600)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movefood()
done()
