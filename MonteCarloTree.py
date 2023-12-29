import numpy as np
from collections import defaultdict
from GoGame import*


class MonteCarloTreeSearchNode():
    def __init__(self, state, parent=None, parent_action=None):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        self._untried_actions = None
        self._untried_actions = self.untried_actions()
        return
    

    def untried_actions(self):

        self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions
    

    def q(self):
        wins = self._results[1]
        loses = self._results[-1]
        return wins - loses
    
    def n(self):
        return self._number_of_visits
    
    def expand(self):
	
        action = self._untried_actions.pop()
        next_state=GoGame(tabuleiro_size=values.grid_size,state=self.state.tabuleiro,turn=self.state.turn,copy=True)
        next_state.print_tabuleiro()
        self.state.print_tabuleiro()
        next_state.move(action[0],action[1])
        next_state.print_tabuleiro()
        self.state.print_tabuleiro()
        child_node = MonteCarloTreeSearchNode(
            next_state, parent=self, parent_action=action)

        self.children.append(child_node)
        return child_node 
    
    def is_terminal_node(self):
        return self.state.is_game_over()
    
    def rollout(self):
        #current_rollout_state = self.state
        current_rollout_state=GoGame(tabuleiro_size=values.grid_size,state=self.state.tabuleiro,turn=self.state.turn,copy=True)
        
        while not current_rollout_state.is_game_over():
            possible_moves = current_rollout_state.get_legal_actions()
            print('1')
            action = self.rollout_policy(possible_moves)
            current_rollout_state.move(action[0],action[1])
            #current_rollout_state = current_rollout_state.move(action[0],action[1])
        return current_rollout_state.game_result() 
    
    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)

    def is_fully_expanded(self):
        return len(self._untried_actions) == 0
    
    def best_child(self, c_param=0.1):
    
        choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]
    
    def rollout_policy(self, possible_moves):
    
        return possible_moves[np.random.randint(len(possible_moves))]
    
    def _tree_policy(self):

        current_node = self
        while not current_node.is_terminal_node():
            
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node
    
    def best_action(self):
        simulation_no = 100
        
        
        for i in range(simulation_no):
            
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        
        return self.best_child(c_param=0.)
    
   

