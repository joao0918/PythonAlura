class Resturante: # Nome de classe sempre com a 1 letra em maiusculo
    restaurantes = []

    """
        Nome = ''
        Categoria = ''
        Ativo = Flase
    
    """
    def __init__(self, Nome, Categoria):
        self.Nome = Nome
        self.Categoria = Categoria
        self.Ativo = False
        Resturante.restaurantes.append(self)

    def descrever(self):
        return f'{self.Nome} | {self.Categoria} | {self.Ativo}'

    def lista_restaurante():
        for restaurante in Resturante.restaurantes:
            print(f'{restaurante.Nome} | {restaurante.Categoria} | {restaurante.Ativo}')

restaurante_porco = Resturante('Porks', 'Peixes')
restaurante_pizza = Resturante('Pizza X', 'Italiana')

Resturante.lista_restaurante()