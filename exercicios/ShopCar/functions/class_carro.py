from time import sleep
class Carro:
    
    carros_adicionados = []

    def __init__(self, marca, ano, valor, km):
        self._marca = marca.upper()
        self._ano = ano
        self._valor = valor
        self._km = km
        self._status = 'A venda'

        Carro.carros_adicionados.append(self)

    def __str__(self):
        return f'{self._marca} | {self._ano} | {self._valor} | {self._km}'
    
    @classmethod
    def lista_carros(cls):
        print(f'{'Marca '.ljust(20)} | {'Ano '.ljust(20)} | {'Valor '.ljust(20)} | {'Quilometragem '.ljust(20)} | {'Status'}')

        carros_ordenados = sorted(cls.carros_adicionados, key=lambda carro: (carro._marca, carro._ano)) # essa função serve para ordenar a lista

        for carro in carros_ordenados:
            print(f'{carro._marca.ljust(20)} | {str(carro._ano).ljust(20)} | {str(carro._valor).ljust(20)} | {str(carro._km).ljust(20)} | {carro._status}')

    @classmethod
    def listar_carros_a_venda(cls):
        print(f'{"Marca ".ljust(15)} | {"Ano ".ljust(15)} | {"Quilometragem ".ljust(15)} | {"Valor ".ljust(15)} | {"Status".ljust(15)}')

        # Filtrando carros com status 'A venda' e 'Em Negociação'
        carros_a_venda = [carro for carro in cls.carros_adicionados if carro._status in ['A venda', 'Em Negociação']]

        # Ordenando por marca (alfabética) e ano (do menor para o maior)
        carros_ordenados = sorted(carros_a_venda, key=lambda carro: (carro._marca, carro._ano))

        # Exibindo os carros
        for carro in carros_ordenados:
            print(f'{carro._marca.ljust(15)} | {str(carro._ano).ljust(15)} | {str(carro._km).ljust(15)} | {str(carro._valor).ljust(15)} | {carro._status.ljust(15)}')

    @classmethod
    def alterar_status_carro_por_marca(cls):
        tentativas = 3
        while tentativas > 0:
            marca_selesionada = input('Digite a marca do carro que deseja alterar: ')
            carro_filtrado = [carro for carro in cls.carros_adicionados if carro._marca.lower() == marca_selesionada.lower()]
            """
            carros_filtrados = []
            for carro in cls.carros_adicionados:
                if carro._marca.lower() == marca_selecionada.lower():
                carros_filtrados.append(carro)

            # UTILIZANDO OPERADOR TERNARIO SIMPLIFICAMOS O CODIGO
            """

            if not marca_selesionada:
                print("Nenhum carro encontrado para essa marca. Tente novamente.")
                tentativas -= 1
                sleep(3)
                continue

            print(f'\nCarros da marca {marca_selesionada.title()}:')
            for idx, carro in enumerate(carro_filtrado):
                print(f'{idx + 1} - {carro}')

            try:
                opcao = int(input(f'Selecione o número do carro que deseja alterar o estado (1-{len(carro_filtrado)}): '))
                if 1 <= opcao <= len(carro_filtrado):
                    carro_selecionado = carro_filtrado[opcao -1]
                    carro_selecionado.alterar_status()
                    print(f'O estado do carro "{carro_selecionado._marca} {carro_selecionado._ano}" foi alterado para: {carro_selecionado._status}')
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")

            sleep(3)
            tentativas -= 1
        if tentativas == 0:
            print('Não foi possível alterar o estado do carro. Voltando ao menu')
        sleep(3)


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
