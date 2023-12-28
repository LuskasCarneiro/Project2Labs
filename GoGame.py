import numpy as np
import values
#from DataTypeSupport import *

class GoGame:
    def __init__(self,tabuleiro_size):
        self.tabuleiro_size=tabuleiro_size
        self.turn=True
        self.make_default_tabuleiro(tabuleiro_size)
        self.score_black=0
        self.score_white=7.5
        self.isend=False
        #self.make_fila_jogadas_default()

    def make_default_tabuleiro(self,tabuleiro_size):
        self.tabuleiro=self.make_matriz(tabuleiro_size)
        self.tabuleiroantes=self.tabuleiro.copy()

    #def make_fila_jogadas_default(self):
    #    self.fila_jogadas=Fila()
    #    for i in range(1):
    #        self.fila_jogadas.push(self.tabuleiro.copy())

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
        
    def move(self,x,y):
        if self.isfree(x,y):
            tabuleiro_com_move=self.tabuleiro.copy()
            tabuleiro_com_move[x][y]=self.value()
            if self.NotOldState(tabuleiro_com_move):
                self.place(x,y)
                #print(self.tabuleiro)
                #print("--------self.tabuleiro pos place-----------")
                self.tabuleiroantes=self.tabuleiro.copy()
                self.check_adjacent_captures(x,y)
                self.capture(x,y)
                self.changeplayerturn()
                self.print_tabuleiro()

    def changeplayerturn (self):
        self.turn = not self.turn

    def NotOldState(self,tabuleiro_com_move):
        return not np.array_equal(tabuleiro_com_move, self.tabuleiroantes)
    
    ####-------------------------------------------- Testar se funciona------------------------------------------####
    def returnWinner(self):
        self.territorio()
        print(f"score black:{self.score_black} score blue: {self.score_white}")

        
    def lib_territorios(self,coor):
        neigh=[]
        for element in [values.EAST,values.SOUTH,values.WEST,values.NORTH]:
            pos=(coor[0]+element[0],coor[1]+element[1])
            if(0<=pos[0]<values.grid_size and 0<=pos[1]<values.grid_size):
                neigh.append(pos) 
            
        return neigh
    
    def territorio(self):
        self.visited=[]
        for i in range(values.grid_size):
            for j in range(values.grid_size):
                if(self.tabuleiro[i][j]==0):
                    neigh=self.lib_territorios((i,j))
                    if(not any(np.array_equal((i,j), item) for item in self.visited)):
                        self.visited.append((i,j))
                        self.cont_terr(neigh)
                    
    def cont_terr(self,neigh):
        stack=list()
        c=1
        flagBlack=False
        flagWhite=False
        for space in neigh:
            stack.append(space)
            while(stack):
                stone=stack.pop()
                
                if(self.tabuleiro[stone[0]][stone[1]]==0 and not any(np.array_equal(stone, item) for item in self.visited)):
                    neigh=self.lib_territorios(stone)
                    c+=1
                    self.visited.append(stone)
                    stack.extend(neigh)       # adicionar os vizinhos todos à lista
                elif(self.tabuleiro[stone[0]][stone[1]]==1):
                    flagBlack=True
                elif(self.tabuleiro[stone[0]][stone[1]]==2):
                    flagWhite=True
                    
        if(flagWhite and flagBlack):
            return 
        elif(flagBlack):
            self.score_black+=c
        elif(flagWhite):
            self.score_white+=c
            
      ####-----------------------------------------------------------------------------------------####



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
    
    def free_pos(self):
        return np.where(self.tabuleiro==values.default)
    
    def return_tabuleiro(self):
        return self.tabuleiro
    
    ##########################################################

    def get_legal_actions(self): 
        '''
        Modify according to your game or
        needs. Constructs a list of all
        possible actions from current state.
        Returns a list.
        '''
        legal_actions=[]
        x,y=self.free_pos()
        for i in range(len(x)):
            if self.isfree(x[i],y[i]):
                tabuleiro_com_move=self.tabuleiro.copy()
                tabuleiro_com_move[x[i]][y[i]]=self.value()
                if self.NotOldState(tabuleiro_com_move):
                    legal_actions.append([x[i],y[i]])
        
        return legal_actions



    def is_game_over(self):
        '''
        Modify according to your game or 
        needs. It is the game over condition
        and depends on your game. Returns
        true or false
        '''
        if self.isfull():
            return True

    def game_result(self):
        '''
        Modify according to your game or 
        needs. Returns 1 or 0 or -1 depending
        on your state corresponding to win,
        tie or a loss.
        '''
        self.score_black=0
        self.score_white=0
        self.territorio()
        if self.score_black>self.score_white:
            return -1
        elif self.score_black==self.score_white:
            return 0
        return -1



