import numpy as np
from linked_piece import *
import values

matriz=np.zeros((values.grid_size,values.grid_size))

print(matriz)

linked=piece(0)
cur_node_hori=linked

for i in range(values.grid_size):
    cur_node_ver=cur_node_hori
    for i in range(values.grid_size):
        cur_node_ver.set_down(piece(0,up=cur_node_ver))
        cur_node_ver=cur_node_ver.get_down()
    cur_node_hori.set_right(piece(0,left=cur_node_hori))
    cur_node_hori=cur_node_hori.get_right()



def print_linked(linked_list):
    if (linked_list!=None):
        print(f"{linked_list.get_value()} {print_linked(linked_list.get_right())} ", end="")
        #if(linked_list.get_down()!=None):
         #   print(f"{linked_list.get_down().get_value()} vert {print_linked(linked_list.get_down().get_right())}")

print_linked(linked)
