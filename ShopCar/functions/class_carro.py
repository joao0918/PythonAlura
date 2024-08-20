class Carro:
    
    carros_adicionados = []

    def __init__(self, marca, ano, valor, km):
        self._marca = marca.title()
        self._ano = ano
        self._valor = valor
        self._km = km
        self._status = 'A venda'

        Carro.carros_adicionados.append(self)

    def __str__(self):
        return f'{self._marca} | {self._ano} | {self._valor} | {self._km}'
    
    @classmethod
    def lista_carros(cls):
        print(f'{'Marca: '.ljust(15)} | {'Ano : '.ljust(15)} | {'Quilometragem: '.ljust(15)} | {'Valor: '.ljust(15)} | {'Status:'}')

        carros_ordenados = sorted(cls.carros_adicionados, key=lambda carro: (carro._marca, carro._ano)) # essa função serve para ordenar a lista

        for carro in carros_ordenados:
            (f'{carro._marca.ljust(15)} | {carro._ano.ljust(15)} | {carro._valor.ljust(15)} | {carro._km.ljust(15)} | {carro._status}')

    def listar_carros_a_venda(cls):
        print(f'{'Marca: '.ljust(15)} | {'Ano : '.ljust(15)} | {'Quilometragem: '.ljust(15)} | {'Valor: '.ljust(15)} | {'Status:'}')

        # aqui estamos filtrando oque desejamos, que seria os carros com status a venda e em negocioação
        carros_a_venda = [carro for carro in cls.lista_carros if carro['status'] in ['A venda', 'Em Negociação']]
                                # aqui esse acessa a lista e a ordena
                                # Ordenando por marca (alfabética) e ano (do menor para o maior)
        carros_ordenados = sorted(carros_a_venda, key=lambda carro: (carro._marca, carro._ano))

        for carro in carros_ordenados:
            (f'{carro._marca.ljust(15)} | {carro._ano.ljust(15)} | {carro._valor.ljust(15)} | {carro._km.ljust(15)} | {carro._status}')

    def alterar_status(self):
        print( """Selecione o Status do carro:
        1 - A venda
        2 - Em negociação
        3 - Vendido""")

        status_carro = int(input('Qual o estado: '))
        if status_carro == 1:
            self._status = 'A Venda'
        elif status_carro == 2:
            self._status = 'Em negociação'
        elif status_carro == 3:
            self._status = 'Vendido'
        else:
            print('Opção selecionada invalida')
