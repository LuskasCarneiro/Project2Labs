import numpy as np

class Attax:
    def __init__(self,tabuleiro_size):
        self.tabuleiro_size=tabuleiro_size
        self.turn=True
        self.make_default_tabuleiro(tabuleiro_size)
        

    def make_default_tabuleiro(self,tabuleiro_size):
        self.tabuleiro=self.make_matriz(tabuleiro_size)
        self.place(0,0)
        self.place(tabuleiro_size-1,tabuleiro_size-1)
        self.changeplayerturn()
        self.place(tabuleiro_size-1,0)
        self.place(0,tabuleiro_size-1)
        self.changeplayerturn()

    def make_matriz(self,tabuleiro_size):
        return np.zeros((tabuleiro_size,tabuleiro_size), dtype=int)
    
    def place(self,x,y):
        self.tabuleiro[x][y]=self.value()

    def remove(self,x,y):
        self.tabuleiro[x][y]=0

    def value(self):
        if self.turn:
            return 2 #brancas
        else:
            return 1 #pretas
    
    def changeplayerturn (self):
        self.turn = not self.turn

    def print_tabuleiro(self):
        print(self.tabuleiro)

    def check_if_end(self):
        if self.isfull():
            return True
        blackx,blacky=np.where(self.tabuleiro==1)
        bluex,bluey=np.where(self.tabuleiro==2)
        if (len(blackx)==0 or len(bluex)==0):
            return True
        return False
    
    def returnWinner(self):
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
        elif total1<total2:
            return 2
        else:
            return 3
        
    def legal_move(self,x,y,movex,movey):
        if not self.isfree(movex,movey) or self.distancia(x,y,movex,movey)>2 or not self.players_piece(x,y):
            return False
        return True
        
        #nao acabada

    def players_piece(self,x,y):
        return self.tabuleiro[x][y]==self.value()

    def distancia(self,x,y,movex,movey):
        difx=abs(x-movex)
        dify=abs(y-movey)
        return max(difx,dify)
    
    def neighbours(self,x,y):
        liminfx=x-1
        liminfy=y-1
        limsupx=x+1
        limsupy=y+1
        if liminfx<0:
            liminfx=0
        if liminfy<0:
            liminfy=0
        if limsupx>(self.tabuleiro_size-1):
            limsupx=self.tabuleiro_size-1
        if limsupy>(self.tabuleiro_size-1):
            limsupy=self.tabuleiro_size-1
        return liminfx, liminfy, limsupx+1, limsupy+1
    
    def neighbours2(self,x,y):
        lista = []
        liminfx=x-2
        liminfy=y-2
        limsupx=x+2
        limsupy=y+2
        if liminfx<0:
            liminfx=0
        if liminfy<0:
            liminfy=0
        if limsupx>(self.tabuleiro_size-1):
            limsupx=self.tabuleiro_size-1
        if limsupy>(self.tabuleiro_size-1):
            limsupy=self.tabuleiro_size-1
        
        lista.append(liminfx)
        lista.append(limsupx+1)
        lista.append(liminfy)
        lista.append(limsupy+1)

        return lista

    def change_neighbours_pieces(self,x,y):
        lx,ly,sx,sy= self.neighbours(x,y)
        for i in range(lx,sx):
            for j in range (ly,sy):
                if self.tabuleiro[i][j]!=0:
                    self.tabuleiro[i][j]=self.value()


    def isjump(self,x,y,movex,movey):
        if self.distancia(x,y,movex,movey)==2:
            return True
        return False

    def make_move(self,x,y,movex,movey):
        if self.legal_move(x,y,movex,movey):
            self.place(movex,movey)
            self.change_neighbours_pieces(movex,movey)
            self.changeplayerturn()
            if self.isjump(x,y,movex,movey):
                self.remove(x,y)
            self.print_tabuleiro()

    def isfree(self,x,y):
        return self.tabuleiro[x][y]==0
    
    def isfull(self):
        x,y=np.where(self.tabuleiro==0)
        if len(x)>0:
            return False
        return True
    
    def ocuppied_pos(self):
        return np.where(self.tabuleiro!=0)
    
    def return_tabuleiro(self):
        return self.tabuleiro
    
    #Se o agente for a cor preta, pesquiso todas as peças pretas no tabuleiro
    def board_pieces(self):
        if self.turn==False:
            turn = 1
        else:
            turn = 2
        lista = []
        for i in range(0,self.tabuleiro_size):
            for j in range(0,self.tabuleiro_size):
                if(self.tabuleiro[i][j]==turn):
                    lista.append((i,j))
        return lista
    
    #Dado uma peça preta no tabuleiro com coordenadas (x,y) pesquiso as possiveis jogadas com essa peça
    def possible_moves(self,x,y):
        lista = []
        limits = self.neighbours2(x,y)
        for k in range(limits[0],limits[1]):
            for s in range(limits[2],limits[3]):
                if(self.tabuleiro[k][s]==0): 
                    lista.append((k,s))
        return lista