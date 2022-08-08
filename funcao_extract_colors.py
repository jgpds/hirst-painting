import colorgram
import turtle
from turtle import Turtle, Screen
import random


def funcao_teste(colors):
    """Função que recebe as cores na formatação do colorgram.extract e retorna as cores no formato de uma lista de tuplas"""
    list_colors = []
    for color in colors:
         color_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
         list_colors.append(color_tuple)
    return list_colors

colors = colorgram.extract('imagem2.png', 10)
print(funcao_teste(colors))