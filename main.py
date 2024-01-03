
from config import args
from ataxx import *
from interface import *
from class_client import *

def main():
    #comunication
    if args['with_comunication']:
        print("player with comunication")
        player = Client(host = args['client_host'], port = args['port'])
        size = player.connect_to_server()

        args['size'] = size
        ag = player.get_ag()
        print("ag: ", ag)
    #no comunicatin
    else:
        print("player without comunication")
        player = None
        ag = None
        size = args['size']

    game_mode = args[args['game_mode']]      #MUDAR AQUI
    game = Ataxx(size)
    initial_state = game.make_s0().copy()

    print(game.get_player_turn())
    print(initial_state)
    interfaceAtaxx(size,game,initial_state,game_mode,client=player,ag=ag)
    
if __name__ == "__main__":
    main()