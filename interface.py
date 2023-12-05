from tkinter import *
from tkinter import ttk
import numpy
import values
from Attax import *



class interfaceAtaxx():
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
                    color='white'
                self.draw(canva,color,x,y)
    

    def draw(self,canva,agentcolor,x,y):
        sqr_size=self.division_size(values.grid_size,values.canva_size)
        canva.create_rectangle(x*sqr_size,y*sqr_size,(x+1)*sqr_size-1,(y+1)*sqr_size-1, fill=agentcolor)    

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
            print(self.mk.return_winner())
            self.root.destroy()
            
    
    def division_size(self,grid,size):
        return int(size/grid)
        
    def make_clean_canvas(self, x=700, y=700):
        base=Tk()
        base.geometry(f'{x}x{y}')
        tela=Canvas(base, bg="white", height=y,width=x)
        tela.pack()
        return base,tela

    def make_clean_frame(self,x=150,y=200):
        base=Tk()
        base.geometry(f'{x}x{y}')
        frame=ttk.Frame(base,padding=10)
        frame.grid()
        return base,frame
    
