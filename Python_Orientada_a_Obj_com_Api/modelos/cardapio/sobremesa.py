from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):

    def __init__(self,nome,price,type,tamanho,description):
        super().__init__(nome,price)
        self.type = type
        self.tamanho = tamanho
        self.description = description

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        pass