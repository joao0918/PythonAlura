class Restaurante:
    lista_de_restaurantes = []

    def __init__(self, Nome, Categoria):
        self._nome = Nome.title()
        self._categoria = Categoria.upper()
        self._ativo = False

        Restaurante.lista_de_restaurantes.append(self)
        

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')

        for show_res in cls.lista_de_restaurantes:
            print(f'{show_res._nome.ljust(25)} | {show_res._categoria.ljust(25)} | {str(show_res.ativo).ljust(25)}')

    @property # decoreitor no python
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
    def alterar_estado(self):
        self._ativo = not self._ativo


