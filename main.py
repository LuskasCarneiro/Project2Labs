#main
from Attax import *
from GoGame import *
import values
from interface import *
from tkinter import *
from MonteCarloTree import *

jogo=Attax(values.grid_size)
interface=interfaceAtaxx(jogo,3)

#jogo= GoGame(values.grid_size,state=None,turn=None)
#interface=interfaceGoGame(jogo)

#while True:
    #x,y = map(int, input("x, y = ").split())
    #jogo.move(x,y)
    #root=MonteCarloTreeSearchNode(state=jogo)
    #selected_node = root.best_action()
    #jogo.move(selected_node[0],selected_node[1])
    
jogo.returnWinner()
    