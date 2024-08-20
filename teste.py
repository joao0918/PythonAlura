from time import sleep
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
        return f'{self._marca} | {self._ano} | {self._valor} | {self._km} | {self._status}'

    @classmethod
    def alterar_estado_carro(cls):
        tentativas = 3
        while tentativas > 0:
            marca_do_carro = input(f'Digite a marca dos carros que deseja listar: ')
            carros_filtrados = [carro for carro in cls.carros_adicionados if carro._marca.lower() == marca_do_carro.lower()]
            
            if not carros_filtrados:
                print("Nenhum carro encontrado para essa marca. Tente novamente.")
                tentativas -= 1
                sleep(3)
                continue

            print(f'\nCarros da marca {marca_do_carro.title()}:')
            for idx, carro in enumerate(carros_filtrados):
                print(f"{idx + 1} - {carro}")

            try:
                opcao = int(input(f'Selecione o número do carro que deseja alterar o estado (1-{len(carros_filtrados)}): '))
                if 1 <= opcao <= len(carros_filtrados):
                    carro_selecionado = carros_filtrados[opcao - 1]
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
            print('Não foi possível alterar o estado do carro.')
        sleep(3)
        cls.back_to_menu()

    def alterar_status(self):
        print("""Selecione o Status do carro:
        1 - A venda
        2 - Em negociação
        3 - Vendido""")

        status_carro = int(input('Qual o estado: '))
        if status_carro == 1:
            self._status = 'A venda'
        elif status_carro == 2:
            self._status = 'Em negociação'
        elif status_carro == 3:
            self._status = 'Vendido'
        else:
            print('Opção selecionada inválida')

    @staticmethod
    def back_to_menu():
        print("Voltando ao menu principal...")

# Exemplo de uso:
carro1 = Carro('Ford', 2019, 30000, 20000)
carro2 = Carro('Audi', 2021, 50000, 15000)
carro3 = Carro('Ford', 2017, 25000, 30000)
carro4 = Carro('BMW', 2018, 45000, 10000)

Carro.alterar_estado_carro()
