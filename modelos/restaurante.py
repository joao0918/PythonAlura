from modelos.avaliacao import Avaliacao

class Resturante: # Nome de classe sempre com a 1 letra em maiusculo
    restaurantes = []

    """
        Nome = ''
        Categoria = ''
        ativo = Flase
    
    """
    def __init__(self, Nome, Categoria):
        self._Nome = Nome.title()
        self._Categoria = Categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Resturante.restaurantes.append(self)

    def __str__(self):
        return f'{self._Nome} | {self._Categoria} | {self._ativo}'

    @classmethod
    def lista_restaurante(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)} ')
        for rest in cls.restaurantes:
            print(f'{rest._Nome.ljust(25)} | {rest._Categoria.ljust(25)} | {str(rest.media_avaliacoes).ljust(25)} | {rest.ativo}')

    @property # decoreitor no python
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, client, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(client, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_de_notas = len(self._avaliacao)

        media = round(soma_das_notas / qtd_de_notas, 1)
        return media


