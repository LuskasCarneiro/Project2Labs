class Fila:
    def __init__(self, first=None):
        self.firstnode=first
        self.lastnode=first
    
    def pop(self):
        self.firstnode=self.firstnode.getnext()

    def push(self,value):
        Nodevalue=Node(value)
        if self.firstnode==None:
            self.firstnode=Nodevalue
            self.lastnode=self.firstnode
        else:
            self.lastnode.setnext(Nodevalue)
            self.lastnode=self.lastnode.getnext()
        
    def getfirst(self):
        return self.firstnode
    
    def getsize(self):
        curnode=self.firstnode
        i=0
        while(curnode!=None):
            curnode=curnode.getnext()
            i+=1
        return i

class Node:
    def __init__(self,value,next=None):
        self.__value=value
        self.__nextnode=next
    
    def getvalue(self):
        return self.__value
    
    def getnext(self):
        return self.__nextnode

    def setnext(self,value):
        self.__nextnode=value

    def setvalue(self,value):
        self.__value=value
        