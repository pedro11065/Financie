from classes.medidas import *

class rampa:

    def __init__(self, dados):
        self.nr : int = dados[0]
        self.tag : str = dados[1]
        self.tipo : str = dados[2]
        self.angulo : float = dados[3]
        self.largura : float = dados[4]
        self.comprimento : float = dados[5]
        self.situacao : bool
        self.recomendacao : str
        

    def verificar(self):
        
        self.angulo = angulo([self.tipo, self.angulo])
        self.largura = largura([self.tipo, self.largura])
        self.comprimento = comprimento([self.tipo, self.comprimento])
        
        self.angulo.verificar(self)
        self.largura.verificar(self)
        self.comprimento.verificar(self)


    
        


