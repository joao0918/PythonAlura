"""Aqui usaremos o conceito de herança onde as outras classe que chamamos de filhas irão herdar ou utilizar o atributo name e price para suas determinadas class"""
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self,nome,price,):
        self._nome = nome
        self._price = price
    
    @abstractmethod
    def aplicar_desconto(self):
        pass
    # Polimorfismo
    # Aqui ele diz para todas as classes que devera ter esse metodo implementado