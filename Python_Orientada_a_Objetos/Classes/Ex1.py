class Resturante: # Nome de classe sempre com a 1 letra em maiusculo
    restaurantes = []
    def __init__(self, Nome, Categoria):
        self.Nome = Nome
        self.Categoria = Categoria
        self.Ativo = False
        Resturante.restaurantes.append(self)

    def __str__(self):
        return f'{self.Nome} | {self.Categoria} | {self.Ativo}'

    def lista_restaurante():
        for restaurante in Resturante.restaurantes:
            print(f'{restaurante.Nome} | {restaurante.Categoria} | {restaurante.Ativo}')

restaurante_porco = Resturante('Porks', 'Italiana')
restaurante_pizza = Resturante('Pizza X', 'Italiana')

if restaurante_porco.Ativo == True:
    print(f'O restaurante esta ativo')
else:
    print('Restaurante desativado')