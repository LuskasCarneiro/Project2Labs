#main
from Attax import *

jogo=Attax(5)

while True:
    x, y = map(int, input("Peça inicial x,y ").split())
    movex, movey = map(int, input("Local Final ").split())
    jogo.make_move(x,y,movex,movey)
    jogo.print_tabuleiro()
    