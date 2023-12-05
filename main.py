#main
from Attax import *
from GoGame import *
import values
from interface import *
from tkinter import *

i=10
jogo=GoGame(values.grid_size)
while i>0:
    x,y = map(int, input("x, y = ").split())
    jogo.make_move(x,y)
    i-=1
jogo.returnWinner()
    