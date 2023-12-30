from tkinter import *
from tkinter import ttk
import numpy
import values
from Attax import *
import time
import random


class interfaceAtaxx():
    def __init__(self,jogo,flag):
        self.mk=jogo
        self.flag=flag
        self.clic1=True
        self.root, self.canva = self.make_clean_canvas(values.canva_size)
        self.draw_default(self.canva)
        #Humano contra humano
        if(self.flag==1): 
            self.root.bind("<Button-1>", self.clicar)

        #Humano contra pc
        if(self.flag==2): 
            self.root.bind("<Button-1>", self.human_agent)

        #pc contra pc
        if(self.flag==3):
            self.root.bind("<Configure>", lambda event=None: self.agent_agent())

        self.root.mainloop()

    def update(self):
        self.draw_default(self.canva)

    def draw_default(self,canva):
        for i in range (0,values.canva_size,self.division_size(values.grid_size,values.canva_size)):
            canva.create_line(i,0,i,values.canva_size, fill="black",width=2)
            canva.create_line(0,i,values.canva_size,i, fill="black",width=2)
        x,y=self.mk.ocuppied_pos()
        matriz=self.mk.return_tabuleiro()
        for x in range(self.mk.tabuleiro_size):
            for y in range(self.mk.tabuleiro_size):
                if matriz[x][y]==1:
                    color=values.color1
                elif matriz[x][y]==2:
                    color=values.color2
                elif matriz[x][y]==0:
                    color='#FFDEAD'
                self.draw(canva,color,x,y)
    

    def draw(self,canva,agentcolor,x,y):
        sqr_size=self.division_size(values.grid_size,values.canva_size)
        canva.create_rectangle(x*sqr_size,y*sqr_size,(x+1)*sqr_size-1,(y+1)*sqr_size-1, fill=agentcolor, outline="#8B4513")    

    def clicar(self, event):
        posicao_grelha = [event.x, event.y]
        posicao_logica = [int(posicao_grelha[0]/self.division_size(self.mk.tabuleiro_size,values.canva_size)),int(posicao_grelha[1]/self.division_size(self.mk.tabuleiro_size,values.canva_size))]
        if not self.mk.check_if_end(): 
            if self.clic1==True:
                self.x=posicao_logica[0]
                self.y=posicao_logica[1]
                self.clic1=False
            else:
                self.movex=posicao_logica[0]
                self.movey=posicao_logica[1]
                self.mk.make_move(self.x,self.y,self.movex,self.movey)
                self.clic1=True
                self.update()
        else:
            print(self.mk.returnWinner())
            self.root.destroy()

    def human_agent(self, event):
        posicao_grelha = [event.x, event.y]
        posicao_logica = [int(posicao_grelha[0]/self.division_size(self.mk.tabuleiro_size,values.canva_size)),int(posicao_grelha[1]/self.division_size(self.mk.tabuleiro_size,values.canva_size))]
        if not self.mk.check_if_end(): 
            if self.clic1==True:
                self.x=posicao_logica[0]
                self.y=posicao_logica[1]
                self.clic1=False
            else:
                self.movex=posicao_logica[0]
                self.movey=posicao_logica[1]
                self.mk.make_move(self.x,self.y,self.movex,self.movey)
                self.clic1=True
                self.update()
                self.agent_behav()
        else:
            print(self.mk.returnWinner())
            self.root.destroy()

    def agent_agent(self):
        if not self.mk.check_if_end(): 
            self.agent_behav()
        else:
            print(self.mk.returnWinner())
            self.root.destroy()

    #Pesquiso as peças da cor que quero no tabuleiro
    def board_pieces(self):
        if self.mk.turn==False:
            turn = 1
        else:
            turn = 2
        lista = []
        for i in range(0,self.mk.tabuleiro_size):
            for j in range(0,self.mk.tabuleiro_size):
                if(self.mk.tabuleiro[i][j]==turn):
                    lista.append((i,j))
        return lista
    
    #Dado uma peça do tabuleiro da cor que eu quero, verifico se através dessa peça existem jogadas possíveis
    def possible_moves(self,x,y):
        lista = []
        limits = self.mk.neighbours2(x,y)
        print(limits)
        for k in range(limits[0],limits[1]):
            for s in range(limits[2],limits[3]):
                if(self.mk.tabuleiro[k][s]==0): 
                    lista.append((k,s))
        return lista


    def agent_behav(self):
        lista = self.board_pieces()
        if lista:
            (x,y) = random.choice(lista)
            print(x)
            print(y)
            moves = self.possible_moves(x,y)
            if moves:
                (movex,movey) = random.choice(moves) #jogada random
                print(movex)
                print(movey)
                self.mk.make_move(x,y,movex,movey)
                self.update()

    #def random(self,fx,fy,tx,ty):
    #    self.mk.make_move(fx,fy,tx,ty)
    #    self.update()
       
    
    def division_size(self,grid,size):
        return int(size/grid)
        
    def make_clean_canvas(self, x=700, y=700):
        base=Tk()
        base.geometry(f'{x}x{y}')
        tela=Canvas(base, bg="black", height=y,width=x)
        tela.pack()
        return base,tela

    def make_clean_frame(self,x=150,y=200):
        base=Tk()
        base.geometry(f'{x}x{y}')
        frame=ttk.Frame(base,padding=10)
        frame.grid()
        return base,frame
    


class interfaceGoGame():
    def __init__(self,jogo):
        self.mk=jogo
        self.clic1=True
        self.root, self.canva = self.make_clean_canvas(values.canva_size)
        self.draw_default(self.canva)
        self.root.bind("<Button-1>", self.clicar)
        self.root.mainloop()

    def update(self):
        self.draw_default(self.canva)

    def draw_default(self,canva):
        for i in range (0,values.canva_size,self.division_size(values.grid_size,values.canva_size)):
            canva.create_line(i+values.go_offset,values.go_offset,i+values.go_offset,values.canva_size+values.go_offset-self.division_size(values.grid_size,values.canva_size), fill="black",width=4)
            canva.create_line(values.go_offset,i+values.go_offset,values.canva_size+values.go_offset-self.division_size(values.grid_size,values.canva_size),i+values.go_offset, fill="black",width=4)
            #time.sleep(5)
        x,y=self.mk.ocuppied_pos()
        matriz=self.mk.return_tabuleiro()
        for x in range(self.mk.tabuleiro_size):
            for y in range(self.mk.tabuleiro_size):
                if matriz[x][y]==1:
                    color=values.color1
                    self.draw(canva,color,x,y)
                elif matriz[x][y]==2:
                    color=values.color2
                    self.draw(canva,color,x,y)
                #elif matriz[x][y]==0:
                    #color='white'
    

    
    def draw(self,canva,agentcolor,x,y):
        sqr_size=self.division_size(values.grid_size,values.canva_size)
        canva.create_oval((x*sqr_size)-(sqr_size/2.5)+values.go_offset,(y*sqr_size)-(sqr_size/2.5)+values.go_offset,((x+1)*sqr_size)-(sqr_size/1.5)+values.go_offset,((y+1)*sqr_size)-(sqr_size/1.5)+values.go_offset, fill=agentcolor, outline="#8B4513")        

    def clicar(self, event):
        posicao_grelha = [event.x, event.y]
        posicao_logica = [int(posicao_grelha[0]/self.division_size(self.mk.tabuleiro_size,values.canva_size)),int(posicao_grelha[1]/self.division_size(self.mk.tabuleiro_size,values.canva_size))]
        if not self.mk.isend: 
            self.x=posicao_logica[0]
            self.y=posicao_logica[1]
            self.mk.move(self.x,self.y,)
            self.update()
        else:
            self.mk.returnWinner()
            self.root.destroy()
            
    
    def division_size(self,grid,size):
        return round(size/grid)
        
    def make_clean_canvas(self, x=values.canva_size, y=values.canva_size):
        base=Tk()
        base.geometry(f'{x+100}x{y+100}')
        #tela=Canvas(base, bg="white", height=y-self.division_size(values.grid_size,values.canva_size),width=x-self.division_size(values.grid_size,values.canva_size))
        tela=Canvas(base, bg="#FFDEAD", height=y,width=x)
        tela.pack()
        return base,tela

    def make_clean_frame(self,x=150,y=200):
        base=Tk()
        base.geometry(f'{x}x{y}')
        frame=ttk.Frame(base,padding=10)
        frame.grid()
        return base,frame