import numpy as np

class Attax:
    def __init__(self,tabuleiro_size):
        self.tabuleiro_size=tabuleiro_size
        self.turn=True
        self.make_default_tabuleiro(tabuleiro_size)
        self.print_tabuleiro()

    def make_default_tabuleiro(self,tabuleiro_size):
        self.tabuleiro=self.make_matriz(tabuleiro_size)
        self.place(0,0)
        self.place(0,tabuleiro_size-1)
        self.changeplayerturn()
        self.place(tabuleiro_size-1,0)
        self.place(tabuleiro_size-1,tabuleiro_size-1)
    
    def make_matriz(self,tabuleiro_size):
        return np.zeros((tabuleiro_size,tabuleiro_size), dtype=int)
    
    def place(self,x,y):
        self.tabuleiro[x][y]=self.value()
    
    def value(self):
        if self.turn:
            return 1
        else:
            return 2
    
    def changeplayerturn (self):
        self.turn = not self.turn

    def print_tabuleiro(self):
        print(self.tabuleiro)

    def check_ifwinner(self):
        if not self.isfull():
            return self.return_winner()
    
    def return_winner(self):
        total1=0
        total2=0
        for i in range (self.tabuleiro_size):
            for j in range (self.tabuleiro_size):
                if self.tabuleiro[i][j]==1:
                    total1+=1
                elif self.tabuleiro[i][j]==2:
                    total2=+2
        if total1>total2:
            return 1
        elif total1==total2:
            return 2
        else:
            return 3
        
    def legal_move(self,x,y,movex,movey):
        if not self.isfree(x,y) or self.distancia(x,y,movex,movey)>2:
            return False
        
        #nao acabada

    def distancia(self,x,y,movex,movey):
        difx=abs(x-movex)
        dify=abs(y-movey)
        return max(difx,dify)
    
    def around_pieces(self,x,y):
        return 0
    #nao acabada

    
    def make_move(self,x,y):
        self.place(x,y)
        self.changeplayerturn()
        #nao acabada

    def isfree(self,x,y):
        return self.tabuleiro[x][y]==0
    
    def isfull(self):
        x,y=np.where(self.tabuleiro==0)
        if len(x)>0:
            return False
        return True



Attax(5)

