import numpy as np
import values

class GoGame:
    def __init__(self,tabuleiro_size):
        self.tabuleiro_size=tabuleiro_size
        self.turn=True
        self.make_default_tabuleiro(tabuleiro_size)
        

    def make_default_tabuleiro(self,tabuleiro_size):
        self.tabuleiro=self.make_matriz(tabuleiro_size)
        self.tabuleirobefore=self.tabuleiro.copy()

    def remove(self,x,y):
        self.tabuleiro[x][y]=values.default

    def get_liberties(self,x,y):
        liberties_vector=[]
        if ((x-1)>=0):
            liberties_vector.append(self.tabuleiro[x-1][y])
        if ((x+1)<self.tabuleiro_size):
            liberties_vector.append(self.tabuleiro[x+1][y])

        if ((y+1)<self.tabuleiro_size):
            liberties_vector.append(self.tabuleiro[x][y+1])
        if ((y-1)>=0):
            liberties_vector.append(self.tabuleiro[x][y-1])

        return liberties_vector
    
    def liberties_are_equal(self,x,y):
        liberties=self.get_liberties(x,y)

        if(liberties[0]==values.default):
            #para lidar com as situacoes onde uma peca e rodeada de 0's, 
            #podemos retornar logo 0 porque se forem todos 0 e falso e se tiver pelo 
            #menos um zero e logo falso poque nao da para capturar e nao
            return False
        
        if (all(i == liberties[0] for i in liberties) and (self.tabuleiro[x][y] != liberties[0])):
            return True
        else: 
            return False
    
    def capture(self,x,y):
        if self.liberties_are_equal(x,y):
            self.remove(x,y)

    def check_adjacent_captures(self,x,y):
        if ((x-1)>=0) and (not self.isfree(x-1,y)):
            self.capture(x-1,y)
        if ((x+1)<self.tabuleiro_size) and (not self.isfree(x+1,y)):
            self.capture(x+1,y)

        if ((y+1)<self.tabuleiro_size) and (not self.isfree(x,y+1)):
            self.capture(x,y+1)
        if ((y-1)>=0) and (not self.isfree(x,y-1)):
            self.capture(x,y-1)


    def value(self):
        if self.turn:
            return 1
        else:
            return 2
        
    def make_move(self,x,y):
        if self.isfree(x,y):
            tabuleiro_com_move=self.tabuleiro.copy()
            tabuleiro_com_move[x][y]=self.value()
            if self.legalmove(tabuleiro_com_move):
                self.tabuleirobefore=self.tabuleiro
                self.place(x,y)
                self.check_adjacent_captures(x,y)
                self.capture(x,y)
                self.changeplayerturn()
                self.print_tabuleiro()

    def changeplayerturn (self):
        self.turn = not self.turn

    def legalmove(self,tabuleiro_com_move):
        return not np.array_equal(tabuleiro_com_move, self.tabuleirobefore)

    def inrange(self,x,y):
        if x<0:
            x=0
        elif x>values.grid_size-1:
            x=values.grid_size-1
        if y<0:
            y=0
        elif x>values.grid_size-1:
            y=values.grid_size-1

        return x,y
        

    def print_tabuleiro(self):
        print(self.tabuleiro)

    def make_matriz(self,tabuleiro_size):
        return np.zeros((tabuleiro_size,tabuleiro_size), dtype=int)
    
    def place(self,x,y):
        self.tabuleiro[x][y]=self.value()

    def isfree(self,x,y):
        return self.tabuleiro[x][y]==values.default
    
    def isfull(self):
        x,y=np.where(self.tabuleiro==values.default)
        if len(x)>0:
            return False
        return True
    
    def isempty(self):
        x,y=np.where(self.tabuleiro==values.default)
        if len(x)!=(values.grid_size**2):
            return False
        return True
    
    def ocuppied_pos(self):
        return np.where(self.tabuleiro!=values.default)
    
    def return_tabuleiro(self):
        return self.tabuleiro


GoGame(5)