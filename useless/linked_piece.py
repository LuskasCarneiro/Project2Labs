class piece:
    def __init__(self,value,right=None,up=None, down=None,left=None):
        self.__value=value
        self.__right=right
        self.__up=up
        self.__down=down
        self.__left=left      

    def __repr__(self):
        return self.__value

    def set_up(self,up_piece):
        self.__up=up_piece
    
    def set_down(self,down_piece):
        self.__down=down_piece
    
    def set_left(self,left_piece):
        self.__left=left_piece
    
    def set_right(self,right_piece):
        self.__right=right_piece

    def set_value(self,value):
        self.__value=value
    
    def get_right(self):
        return self.__right
    
    def get_left(self):
        return self.__left
    
    def get_up(self):
        return self.__up
    
    def get_down(self):
        return self.__down
    
    def get_value(self):
        return self.__value