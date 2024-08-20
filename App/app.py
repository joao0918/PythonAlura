# IMPORTAÇÕES
from OO_PY_RESTOURANTE.class_restaurante import Restaurante
import os
from time import sleep

# COMPLEMENTOS DO SISTEMA
def clear():
    os.system('cls')
def display_program_name():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    \n""")
def display_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def back_to_menu():
    clear()
    main()
def option_invalid():
    clear()
    print('Opção invalida...')
    sleep(1)
    back_to_menu()
def show_subtitle(texto):
    clear()
    print(f'{texto}\n')
          
# PROGRAMA

def register_restaurant():
    show_subtitle('Cadastre novos restaurantes:')

    nome_do_restaurante = input('digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    novo_restaurante = Restaurante(nome_do_restaurante, categoria_do_restaurante)

    print('Guardando dados...')
    sleep(2)
    print('\nRestaurante criado com sucesso!!!')

    print('Voltando ao menu.')
    sleep(3)
    back_to_menu()

def display_restaurant():
    show_subtitle('Aqui esta a lista de restaurantes:')
    Restaurante.listar_restaurantes()

    input('\nAperte ENTER para sair')
    back_to_menu()

def change_status():
        show_subtitle('Ativar/Desativar Restaurante:')

        
        
        tentativas = 3
        while tentativas > 0:
            nome_do_restaurante = input(f'Digite o nome do restaurante que deseja altera o estado: ')
            restaurante_select = False
            for restaurante in Restaurante.lista_de_restaurantes:
                if restaurante._nome.lower() == nome_do_restaurante.lower():
                    restaurante.alterar_estado()
                    print(f'O estado do restaurante "{restaurante._nome}" foi alterado para: {restaurante.ativo}')
                    restaurante_select = True
                    break  
            if restaurante_select:
                break
            else:
                print("Restaurante não encontrado. Tente novamente")
                sleep(3)
            
            tentativas -= 1

        if restaurante_select == False:
            print('Restaurante não esta dentro do nosso sistema.')
        sleep(3)
        back_to_menu()

def cloase_program():
    print('\nFinalizando programa...')
    sleep(2)
    close()

def choose_option():
    """Nessa função ele colhera a informação do usuario e redicionara para outro campo"""
    try: 
        option_select = int(input('Escolha uma opção: '))

        if option_select == 1:
            register_restaurant()

        elif option_select == 2:
            display_restaurant()

        elif option_select == 3:
            change_status()
        else:
            cloase_program()
    except:
        option_invalid()



def main():
    os.system('cls')
    display_program_name()
    display_options()
    choose_option()

if __name__ == '__main__': 
    main()