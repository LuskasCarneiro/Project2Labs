import numpy as np
from values import *

class GoGame:
    def __init__(self,tabuleiro_size):
        self.tabuleiro_size=tabuleiro_size
        self.turn=True
        self.make_default_tabuleiro(tabuleiro_size)
        

    def make_default_tabuleiro(self,tabuleiro_size):
        self.tabuleiro=self.make_matriz(tabuleiro_size)
        self.print_tabuleiro()

    def remove(self,x,y):
        self.tabuleiro[x][y]=0

    def value(self):
        if self.turn:
            return 1
        else:
            return 2
    
    def changeplayerturn (self):
        self.turn = not self.turn

    def print_tabuleiro(self):
        print(self.tabuleiro)

    def make_matriz(self,tabuleiro_size):
        return np.zeros((tabuleiro_size,tabuleiro_size), dtype=int)
    
    def place(self,x,y):
        self.tabuleiro[x][y]=self.value()
