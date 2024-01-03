from tkinter import *
from tkinter import ttk

import values
import time
from config import args


class interfaceAtaxx():

    def __init__(self, size, game, initial_state, type_game, client= None, ag = None):

        self.size = size
        self.game = game
        self.state = initial_state

        if client:
            self.comunication = True
            self.client = client
            self.ag=ag      #se é agente 1 ou 2
            self.first=True

        #first click
        self.click=True
        self.root, self.canva = self.make_clean_canvas(values.canva_size)
        self.draw_default(self.canva)
        

        if(type_game==1):   self.root.bind("<Button-1>", self.clicar)
        #Humano contra pc
        elif(type_game==2):   self.root.bind("<Button-1>", self.human_agent)
        #pc contra pc
        elif(type_game==3):
            if client:
                self.play_as_random_client()
            else:
                self.play_as_random(initial_state)

        else:
            print("Flag not defined")
    
        self.root.mainloop()

    def get_last_move(self):
        return self.movex, self.movey
    
    def close_window(self):
        self.root.destroy()

    def update(self):
        self.draw_default(self.canva)
    
    def update_state(self,state):
        self.state = state

    def draw_default(self,canva):
        for i in range (0,values.canva_size,self.division_size(values.grid_size,values.canva_size)):
            canva.create_line(i,0,i,values.canva_size, fill="black",width=2)
            canva.create_line(0,i,values.canva_size,i, fill="black",width=2)
        #x,y=self.game.ocuppied_pos()
        matriz=self.state
        for x in range(self.size):
            for y in range(self.size):
                if matriz[x][y]==-1:
                    color=values.color1
                elif matriz[x][y]==1:
                    color=values.color2
                elif matriz[x][y]==0:
                    color='#FFDEAD'
                else:# matriz[x][y]==3:
                    color='red'
                self.draw(canva,color,x,y)
    

    def draw(self,canva,agentcolor,x,y):
        sqr_size=self.division_size(values.grid_size,values.canva_size)
        canva.create_rectangle(x*sqr_size,y*sqr_size,(x+1)*sqr_size-1,(y+1)*sqr_size-1, fill=agentcolor, outline="#8B4513")    

#Human x Human
    def clicar(self, event):
        posicao_grelha = [event.x, event.y]
        posicao_logica = [int(posicao_grelha[0]/self.division_size(self.size,values.canva_size)),int(posicao_grelha[1]/self.division_size(self.size,values.canva_size))]
        if not self.game.check_if_end():
            if self.clic1==True:
                self.x=posicao_logica[0]
                self.y=posicao_logica[1]
                self.clic1=False
            else:
                self.movex=posicao_logica[0]
                self.movey=posicao_logica[1]
                self.game.make_move(self.x,self.y,self.movex,self.movey)
                self.clic1=True
                self.root.update()
        else:
            print(self.game.returnWinner())
            self.root.destroy()

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
    
#without client
    def play_as_random(self,s):
        def play_next_move(s):
            if not self.game.is_finished(s):
                move = self.game.get_random_move(s)
                s = self.game.play_move(move[0], move[1], move[2], move[3], s)
                print(self.game.get_player_turn())
                print(s)
                self.update_state(s)
                self.update()
                self.game.change_turn()
                 #this works as a cilce with time.slepp of 1000 miliseconds
                self.root.after(args['time_between_moves'], lambda: play_next_move(s))   
            else:
                print(self.game.winner(s))
                self.root.title("Game Over - Winner: " + str(self.game.winner(s)))

        self.update_state(s)
        self.update()
        self.root.after(args['time_between_moves'], lambda: play_next_move(s))
        self.root.mainloop()


#whith client
    def play_as_random_client(self):
        def play_next_move(s):
            if not self.game.is_finished(s):    #como se fosse while

                if self.ag == 1 or not self.first:
            # 1_PLAY & SEND___________________________________
                    move = self.game.get_random_move(s)
                    s = self.game.play_move(move[0], move[1], move[2], move[3], s)
                    #JANELA
                    self.update_state(s)
                    self.update()
                    self.root.update_idletasks()
                    #TERMINAL
                    print(self.game.get_player_turn())
                    print(s)
        
                    #SEND MOVE
                    move_message = self.client.stringify_move_ataxx(move[0], move[1], move[2], move[3])
                    time.sleep(1)
                    self.client.client_socket.send(move_message.encode())
                    print("Send:", move_message)
                    self.game.change_turn()


            # 2_RECEIVE & PLAY___________________________________
                    # play as the other side
                    print("2: ", self.game.get_player_turn())
                    response = self.client.client_socket.recv(1024).decode()
                    print(f"Server Response1: {response}")
                    if "END" in response:
                        return
    
                    move = self.client.decode_stringify_move_ataxx(response)
                    s = self.game.play_move(move[0], move[1], move[2], move[3], s)

                    self.update_state(s)
                    self.update()
                    print(self.game.get_player_turn())
                    print(s)
                    self.root.update_idletasks()

                    self.game.change_turn()
    
                else:
                    # the function that plays for the adversary
                    self.first = False
                    print(": ", self.game.get_player_turn())
                    response = self.client.client_socket.recv(1024).decode()
                    print(f"Server Response2: {response}")
    
                    if "END" in response:
                        return
    
                    move = self.client.decode_stringify_move_ataxx(response)
                    s = self.game.play_move(move[0], move[1], move[2], move[3], s)
                    self.update_state(s)
                    self.update()
                    self.root.update_idletasks()
                    print(self.game.get_player_turn())
                    print(s)

                    self.game.change_turn()
    
                # Schedule the next move after a delay (in milliseconds)
                time.sleep(1)
                self.root.after(args['time_between_moves'], lambda: play_next_move(s))
            else:
                print(self.game.winner(s))
                self.root.title("Game Over - Winner: " + str(self.game.winner(s)))
                self.client.client_socket.close()
                return

        # Your existing code for receiving the initial state from the server goes here
        self.update_state(self.state)
        self.update()
        self.root.after(args['time_between_moves'], lambda: play_next_move(self.state))
        self.root.mainloop()



