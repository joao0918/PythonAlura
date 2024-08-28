from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self,nome,price,description):
        super().__init__(nome,price) # obj especial, permite que acesse informações de outra classe
        self.description = description

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._price -= (self._price * 0.05)