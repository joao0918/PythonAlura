from Banco.classes import Banco

class Agencia(Banco):
    def __init__(self,name,eddress,numero):
        super().__init__(name,eddress)
        self._numero = numero