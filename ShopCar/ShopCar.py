from functions.class_carro import Carro
from time import sleep
from os import system

carro1 = Carro('Ford', 2019, 30000, 20000)
carro2 = Carro('Audi', 2021, 50000, 15000)
carro3 = Carro('Ford', 2017, 25000, 30000)
carro4 = Carro('BMW', 2018, 45000, 10000)

def clear():
    system('cls')
def logo_app():
    print("""         ▄▄                                                         
 ▄█▀▀▀█▄███                                ▄▄█▀▀▀█▄█                
▄██    ▀███                              ▄██▀     ▀█                
▀███▄    ███████▄   ▄██▀██▄▀████████▄    ██▀       ▀▄█▀██▄ ▀███▄███ 
  ▀█████▄██    ██  ██▀   ▀██ ██   ▀██    ██        ██   ██   ██▀ ▀▀ 
▄     ▀████    ██  ██     ██ ██    ██    ██▄        ▄█████   ██     
██     ████    ██  ██▄   ▄██ ██   ▄██    ▀██▄     ▄▀█   ██   ██     
█▀█████▀████  ████▄ ▀█████▀  ██████▀       ▀▀█████▀▀████▀██▄████▄   
                             ██                                     
                           ▄████▄                                   
""")
def close():
    clear()
    print('Obrigado pela confiança, volte logo...')
    sleep(3)
    exit()
def exibir_erro(message):
    clear()
    print(message)
    sleep(3)
def exibir_title(mensage):
    clear()
    print(f'{mensage}\n')
def lobby(time=3):
    sleep(time)
    input('\nAperte ENTER para voltar.')
    exibir_title('Voltando para o menu.')
    sleep(1)
    main()


def select_option():
    logo_app()
    print("""Slecione uma das opções a baixo: 
    1 - Adcionar carro.
    2 - Listar carros
    3 - Listar Carros a venda
    4 - Mudar Status do carro
    5 - Sair""")

    opcao = int(input('Opção selecionada: '))

    try: 
        if opcao == 1:
            adcionar_carro()
        elif opcao == 2:
            mostrar_carros()
        elif opcao == 3:
            carros_a_venda()
        elif opcao == 4:
            mudar_status_do_carro()
        elif opcao == 5:
            close()
        else:
            exibir_erro('Opção Invalida, Tente novamente.')
            main()

    except ValueError:
        exibir_erro('Opção Invalida, Tente novamente.')
        main()

def adcionar_carro():
    exibir_title('Adicione um carro novo na loja')
    
    # Só saira do loop apos todos os dados forem inseridos
    while True:
        try:
            marca_do_carro = input('Qual a Marca do carro: ').strip()
            if not marca_do_carro:
                raise ValueError("Marca do carro não pode estar em branco.")
            
            # Obter e verificar o ano do carro
            ano_do_carro = input('Qual o ano do carro: ').strip()
            if not ano_do_carro:
                raise ValueError("O ano do carro não pode estar em branco.")
            ano_do_carro = int(ano_do_carro)  # Convertendo após verificação
            
            # Obter e verificar o valor do carro
            valor_do_carro = input('Qual o valor de venda: ').strip()
            if not valor_do_carro:
                raise ValueError("O valor de venda não pode estar em branco.")
            valor_do_carro = int(valor_do_carro)  # Convertendo após verificação
            
            # Obter e verificar a quilometragem
            km_rodado = input('Quantos quilômetros esse carro já rodou: ').strip()
            if not km_rodado:
                raise ValueError("A quilometragem não pode estar em branco.")
            km_rodado = int(km_rodado)  # Convertendo após verificação

            # Se todos os dados forem válidos, saímos do loop
            break

        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira os dados corretamente.")

    new_car = Carro(marca_do_carro, ano_do_carro, valor_do_carro, km_rodado)
    print(f"\nCarro {new_car._marca} adicionado com sucesso!")
    lobby(1)

def mostrar_carros():
    exibir_title('Aqui está todos os carros')
    Carro.lista_carros()
    lobby(2)

def carros_a_venda():
    exibir_title('Carros a venda')
    Carro.listar_carros_a_venda()
    lobby(5)

def mudar_status_do_carro():
    exibir_title('Alterar Status do carro')
    Carro.alterar_status_carro_por_marca()
    lobby(2)

def main():
    clear()
    select_option()
    
if __name__ == '__main__':
    main()