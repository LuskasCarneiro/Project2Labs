import socket
import time
import traceback
from config import args

Game="A4x4" # "A6x6" "G7x7" "G9x9" "A5x5"

#O servidor está a escuta (de 2 agentes apenas)
#O Servidor só recebe jogadas  e re_envia para o adversário

def start_server(host=args['server_host'], port=args['port']):
    #inicializar socket && atrubuir host e porta && ficar a escuta de 2 agentes
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    server_socket.bind((host, port))
    server_socket.listen(2)                
    print("Waiting for two agents to connect...")

    #recebe entrada do primeiro agente e respoonde lhe o jogador(AG1) e o jogo que vai ser jogado (A4x4)
    agent1, addr1 = server_socket.accept()
    print("Agent 1 connected from", addr1)
    bs=b'AG1 '+Game.encode()
    agent1.sendall(bs)   #destinatário.sendall(mensagem)

    #recebe entrada do segundo agente e respoonde lhe o jogador(AG2) e o jogo que vai ser jogado (A4x4)
    agent2, addr2 = server_socket.accept()
    print("Agent 2 connected from", addr2)
    bs=b'AG2 '+Game.encode()
    agent2.sendall(bs)    

    #guarda os agentes em agents e define o indice do agente atual(agents[0])
    agents = [agent1, agent2]
    current_agent = 0

    #numero da jogada
    jog=0
    #Apenas quando já estão os dois agentes conectados:
    #Inicia troca de mensagens entre os agentes(pelo servidor) relacionadas com o jogo
    while True:
        try:
            #Recebe e descodifica a mensagem/JOGADA do 1º agente a entrar no server = agents[0]
            #1024 bytes->max espaço de mensagem && .recv()->recebe mensagem
            data = agents[current_agent].recv(1024).decode()
            if not data:
                print("server didn't receive data")
                break

            # Process the move (example: "MOVE X,Y")
            print(current_agent, " -> ",data)
            jog = jog+1
            

            # Send back a response: - VALID or INVALID to the sender, if the move is(n´t) valid
            if is_valid_move(data):#------por fazer (verificar função)
                #Se for válida, envia a jogada para o agente adeversário
                agents[1-current_agent].sendall(data.encode())
                print("server has sent")
            else:
                print("invalid move")
               #agents[current_agent].sendall(b'INVALID')

            # Switch to the other agent
            current_agent = 1-current_agent  #mudar no jogo também?
            time.sleep(1)

        except Exception as e:
            print("Error:", e)
            traceback.print_exc()
            break
    
    print("\n-----------------\nGAME END\n-----------------\n")
    time.sleep(1)
    agent1.close()
    agent2.close()
    server_socket.close()

def is_valid_move(move):
#para verificar a validade tenho que ter um jogo inicalizado no servidor
    return True #por fazer com game.valid_move()

if __name__ == "__main__":
    start_server()
