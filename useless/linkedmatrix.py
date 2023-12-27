from linked_piece import *
class linkedmatrix:
    def __init__(self, size):
        self.__size=size
        self.__inicial_piece=piece(1)

    def make_default_matrix(self):
        self.__currentpiecehorizontal=self.__inicial_piece
        for i in range(self.__size):
            self.__currentpiecevertical=self.__currentpiecehorizontal
            for k in range(self.__size):  
                self.__currentpiecevertical.set_down(value=piece(1),up=self.__currentpiecevertical)
                self.__currentpiecevertical=self.__currentpiecevertical.get_down()
            self.__currentpiecehorizontal.set_right(value=piece(1),left=self.__currentpiecehorizontal)
            self.__currentpiecehorizontal=self.__currentpiecehorizontal.get_right()

    def setup(node,upnde):
        node.set_up(upnde)
        node.get_up().set_down(node)

                







