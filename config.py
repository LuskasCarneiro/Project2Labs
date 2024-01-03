args = {
    'white': 1,
    'black': -1,
    'white_rel_pos': [(0,0),(0,0)],         #posição relativa em relação ao cantos  # not veryfing the rel_positions, it needs to be done right -> da esquerda pa a direita ->
    'black_rel_pos': [(0,0),(0,0)],         #posição relativa em relação aos cantos
    'port': 12382,                          #porta do servidor
    'server_host':'localhost',              #host do servidor
    'client_host':'localhost',              #host do cliente
    'agent_vs_agent': 3,                    #flag para modo de jogo entra aqui
    'agent_vs_human': 2,
    'human_vs_human': 1,
    'game_mode': 'agent_vs_agent',          #modo de jogo  MUDAR AQUI
    'with_comunication': False,             #flag para comunicação entra aqui
    'size': 4,                               #tamanho do tabuleiro
    'time_between_moves': 1000              #tempo entre movimentos em milisegundos
    }

#ALTERAÇÕES DE CONFICGURAÇOES SÃO FEITAS AQUI
    #acrescentar chave caso o jogo queira receber um configuração inicial especifica