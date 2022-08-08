import colorgram
import turtle
from turtle import Turtle, Screen
import random
from funcao_extract_colors import funcao_teste

colors = colorgram.extract('imagem2.png', 10)
list = funcao_teste(colors)
tim = Turtle()
screen = Screen()


tim.shape("turtle")
tim.color("red", "pink")
direction = ["right", "left", "forward", "back"]
tim.speed(20)
tim.pensize(1)
turtle.colormode(255)
tim.hideturtle()
tim.penup()
tim.goto(-280,-280)
i = -280
for _ in range(15):
    for _ in range(15):
        tim.dot(15, random.choice(list))
        tim.forward(40)
        print(tim.pos())
    i += 40.0
    tim.goto(-280, i)



screen.exitonclick()
