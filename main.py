#main
from Attax import *
from GoGame import *
import values
from interface import *
from tkinter import *

jogo=GoGame(values.grid_size)
while True:
    x,y = map(int, input("Introduz qualquer merda porfavor ").split())
    jogo.make_move(x,y)
    