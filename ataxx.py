# + clicar vs clicar + clicar vs agente + agente vs agente

                        #VERIFICAR ACTIONS SPACES NULOS, JOGADAS INVALIDAS, manualmente


import numpy as np
from config import args

'''
A class Ataxx recebe Estado, opera sobre ele,e retorna Estado "operado" 
assim no montecarlo apenas um objeto será criado, e copiar diferentes estados.
no Go, existe um if, que é usado quando o jogo começa noutro estado, 
mas mesmo aí um novo objeto tem que ser criado, pois a ativação deste if 
depende da inicialização

penso que isto também facilitará a interface com o jogo, pois é só dar a matriz á interface
'''

class Ataxx:
    #compliquei, bastava self.state = state e uma função 
    #self.receive_state que fazia update do estad recebido
    # aplicava o move e devolvia o estado para fora do objeto

    def __init__(self,size): #flag para modo de jogo entra aqui
        #inicializar
        self.size = size
        self.args = args
        self.turn = 'white'
        self.last_nine = [] #this is for the threefold repetition rule(like chess)

    def make_s0(self):
        '''
        esta função cria o estado inicial do jogo
        é tambem responsável por colocar as peças nos cantos ou em posições relativas aos cantos dependendo do pedido
        FALTA PADRONIZAR OS BLOCOS NÃO JOGÁVEIS -> FUNÇÃO MAFALDA
        '''
        matrix = np.zeros((self.size, self.size), dtype=int)
        ''' also add to white corners relative position'''
        matrix[0 + self.args['white_rel_pos'][0][0]][0 + self.args['white_rel_pos'][0][1]] = self.args['white']
        matrix[self.size-1 + self.args['white_rel_pos'][1][0]][self.size-1 + self.args['white_rel_pos'][1][1]] = self.args['white'] 
        ''' also add to black corners relative position'''
        matrix[self.size-1 + self.args['black_rel_pos'][0][0]][0 + self.args['black_rel_pos'][0][1]] = self.args['black']
        matrix[0 + self.args['black_rel_pos'][1][0]][self.size-1 + self.args['black_rel_pos'][1][1]] = self.args['black']

        return matrix

    def place(self,x,y,state):
        #colocar peça em x,y
        state[x][y] = self.args[self.turn]
        return state
        
    def remove(self,x,y,state):
        #remover peça em x,y -> will be used when jumping
        state[x][y] = 0
        return state

    def get_state(self):
        #return actual state -> necessary for algorithms I think
        return self.state
    
    def get_player_turn(self):
        #ALTERAR ISTO PARA DE ACORDO COM O  NUMERO DE PEÇAS
        return self.turn 
    
    def change_turn(self):
        # não vai ser chamada em numa das funções move mas, mas sim externamente para termos mais controlo
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

    def distance(self,x,y,movex,movey):                 
        # distance between two points
        difx=abs(x-movex)
        dify=abs(y-movey)
        return max(difx,dify)
    
    def isjump(self,x,y,movex,movey):
        #check if the move is a jump
        return self.distance(x,y,movex,movey)==2    
    
    def isfree(self,x,y,state):                               
        # check if a position is free
        return state[x][y]==0
    
    def infect_neighbours(self,x,y,state):
        #infection space has radius 1 from final moved x, y
        infection_space = self.radius_space(x,y,1)
        for (line,col) in infection_space:
            if state[line][col] != 0:
                self.place(line,col,state)   #!!! IS JUST A CHECK !!!    CHANGE TO PLACE
        #return state talvez não precisepor ser um objeto numpy(ou seja as alteraçoes ficam guardadas) 

    def radius_space(self,x,y,radius): 
        # all the possible moves for a pick x y
        #the radius is either 1 or 2
        radius_space = []   
        # check radius space
        bottom = x+radius
        left = y-radius
        top = x-radius
        right  = y+radius
        # check if the radius space is inside the board
        while left<0:
            left+=1
        while top<0:
            top+=1
        while right > (self.size-1):
            right-=1
        while bottom > (self.size-1):
            bottom-=1
        # from radius space select all positions (empty included)
        for line in range(top,bottom+1):           
            for col in range(left, right+1):        
                radius_space.append((line,col)) 
        #return all
        return radius_space  
    
    def possible_picks(self,state):                           
        # all the possible picks for the player
        x, y = np.where(state == self.args[self.turn])
        return list(zip(x,y))
    
    def picked_action_space(self,x,y,state):
        #action space from picked x y (radius 2 and 1)
        picked_action_space = []
        aux = self.radius_space(x,y,2)
        for (line,col) in aux:
            if self.isfree(line,col,state):
                picked_action_space.append((line,col))
        return picked_action_space  #retorna tuplo (movex,movey)
            
    def action_space(self,state):
        #return all action space for the current state and player
        #lista de "quadruplos"
        all_actions = []
        picks = self.possible_picks(state)
        for (x,y) in picks:
            for (movex,movey) in self.picked_action_space(x,y,state):
                if movex is not None and movey is not None:# ! tem que ser com not none, porque severificarmos só com (if move) e move=0 ele não entra pois 0 = false
                    all_actions.append((x,y,movex,movey))
        return all_actions    
    

    def play_move(self, pickX, pickY, moveX, moveY, state):
        self.add_to_lastnine(state) #to keep checking the threefold repetition rule
        #movimento já vem verificado indiretamente pelo action space
        self.place(moveX, moveY,state)
        if self.isjump(pickX, pickY, moveX, moveY):
            self.remove(pickX, pickY,state)
        self.infect_neighbours(moveX, moveY,state)
        return state    #!!!!
    
    def verify_move(self, pickX, pickY, moveX, moveY, state):
        if (pickX, pickY, moveX, moveY) in self.action_space(state):
            return True
        return False
    
    def get_random_move(self,state):
        #Random agent
        #fazer return a random move from action space,
        #não aplicar o move, apenas retornar, devido à comunicação
        action_space = self.action_space(state)
        (x,y,movex,movey) = action_space[np.random.randint(0,len(action_space))]
        return (x,y,movex,movey)


    #__________END_GAME_FUNCS__________
     ## threefold_repetition_rule - um dos motivos de empate
    def add_to_lastnine(self,state):
        novo = state.copy()
        if (len(self.last_nine)==9):
            self.last_nine.pop(0)
            self.last_nine.append(novo)
        else:
            self.last_nine.append(novo)

    def is_threefold_repetition_rule(self):
        dic={}
        if self.last_nine and len(self.last_nine)==9:
            for i in self.last_nine:
                tuplo = tuple(map(tuple, i))
                if tuplo in dic.keys():
                    dic[tuplo] += 1
                else:
                    dic[tuplo] = 1

            for tuplo in dic.keys():
                if dic[tuplo]>=3:
                    return True
        return False

    
    def count(self,color,state):
        x, _ =np.where(state == color)
        return len(x)
    
    def is_finished(self, state):
        if self.isfull(state) or self.is_stuck(state) or self.is_threefold_repetition_rule():
            return True
        return False
    
    def isfull(self, state):
        #retornar vencedor em winner
        x, _ =np.where(state == 0)
        if len(x)>0:
            return False
        return True
    
    def is_stuck(self, state):
        #IMPORTANT: NO IS FULL
        if len(self.action_space(state)) == 0 and (not self.isfull(state)):
            return True # mudar jogador então
        return False
    
    
    def winner(self, state):
        if self.isfull(state):
            print("Game is finished by full board!")
            if (self.count(self.args['white'],state) - self.count(self.args['black'],state) > 0):
                print("_WHITE_WINS_")
                return "WHITE"
            elif (self.count(self.args['white'],state) - self.count(self.args['black'],state) < 0):
                print("_BLACK_WINS_")
                return "BLACK"
            else:
                print("_DRAW_")
                return "DRAW"

        elif self.is_stuck(state):
        #Para 4x4 e 6x6
        #se eu estou preso, meu adeversário ou está preso também(full), ou ainda pode jogar.
        #se ele pode jogar, então iria jogar até o tabuleiro ficar cheio, 
        #pois o que falta, só ele pode jogar.
        #Assim, so numero de peças futuro dele for maior que o meu presente, ele ganha
        #por isso o numero de peças do adeversário em stuck, é a contar com 
        #as peças(que estão vazias) que ele iria jogar até o tabuleiro ficar cheio
            print(f"Game is finished! {self.get_player_turn()} is stuck.")
            color_turn = self.get_player_turn()
            self_count = self.count(self.args[color_turn],state)
            opponent_possible_count = self.size*self.size - self_count
            if self_count > opponent_possible_count:
                print("_",color_turn.upper(),"_WINS_")
            elif self_count < opponent_possible_count:
                if color_turn == 'white':
                    print("_BLACK_WINS_")
                    return "BLACK"
                else:
                    print("_WHITE_WINS_")
                    return "WHITE"
            else:
                print("_DRAW_")
                return "DRAW"
            
        elif self.is_threefold_repetition_rule():
            #????? vou por draw, pois não quero que o modelo aprenda a ganhar por esta regra 
            print("Game is finished by threefold repetition rule!")
            print("_DRAW_")
            return "DRAW"
            



