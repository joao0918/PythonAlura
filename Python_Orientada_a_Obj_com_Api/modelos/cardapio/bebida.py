from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self,nome,price,tamanho):
        super().__init__(nome,price)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._price -= (self._price * 0.05)