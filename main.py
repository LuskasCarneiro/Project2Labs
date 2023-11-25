#main
from Attax import *
import values
from interface import *
from tkinter import *

jogo=Attax(values.grid_size)
inter=interfaceAtaxx(jogo)

while True:
    inter.canva.bind('<Button-1>',x=inter.clicar)
    movex, movey = inter.clicar()
    jogo.make_move(x,y,movex,movey)
    inter.update()
    jogo.print_tabuleiro()


    