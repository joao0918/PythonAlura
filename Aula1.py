"""
ALURA   

Aqui começa nossa jornada na alura, nessa 1 fase.
Vamos fazer um prjeto de um aplicativo de entrega de comida, e vamos implementar uma dessas partes.
"Sabor Express"

Forma de manter os dados da aplicação.
Vamos fazer a parte do back-And

# Boas pratica de variaveis link: https://encurtador.com.br/BJMUW
e também questao de aspas sempre utilizar a que foi iniciada ou melhor usar sempre a mesma.

pass = passar

Utilizamos aspas tripas para textos grandes, com varias linhas.

"""

import os # as nome_qualquer voce escolhe um nome para chamar esse function

""" Dicionarios

Aqui diferente da lista usamos chave e valor como voce pode ver a baixo.
Podendo ter um poder maior sobre nossos restaurantes.
"""
restaurantes = [{'nome': 'japanHouse', 'categoria': 'Japonesa', 'ativo': False}, # true or false são valores boleanos
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]

def volta_ao_menu():
    input('\nDigite uma tecla para voltar ao menu')
    main()
    
def finalizar_app(): # "def" serve para criar um função
    exibir_subtitulo('Encerrando programa...\n') # limpa o terminal caso caia para essa function

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def opcao_invalida():
    print('Opção Inválida...\n')
    input('PRESS ENTER TO RETURN')
    volta_ao_menu()

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    \n""")

def exibir_opcoes(): # ctrl + "{" = jogar para o lado direito
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

""" LISTA

podemos armazenar uma coleção de dados, dentro de uma lista.

lsia = [sowsow,jddo]
"""
def cadastrar_nova_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    # Nessa parte atualizamos oque estava antes que era so uma lista p/ um dicionario
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria' :categoria_do_restaurante, 'ativo': False} # e cadastramos cada opçao
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    volta_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Aqui esta a lista de restaurantes:\n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        restaurante_ativo = restaurante['ativo']
        print(f'-{nome_restaurante} | {categoria_restaurante} | {restaurante_ativo}')

    volta_ao_menu()

""" NOT

No not ele altera o valor de True para False e o contrario
ex: not False
resultado: True
"""

""" TERNARIO

é uma forma concisa de escrever uma expressão condicional de forma simplificada

EX: mensagem = f'O restaurante foi {nome_restaurante} foi ativado com sucesso' if buscando['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
        print(mensagem)
"""

""" MATCH OU IF
O 'IF' nos proporciona uma maneira eficaz de tomar decisões simples ou complexas em nosso código, 
adaptando o comportamento do programa de acordo com as circunstâncias determinadas. Ao usar 'MATCH', 
podemos simplificar a lógica do código em situações que envolvem múltiplos padrões complexos. 
Ela oferece uma estrutura mais legível, especialmente quando temos diversos casos a serem tratados.
"""
def alterar_estado_restaurante():
    exibir_subtitulo('Aternando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    
    #validação do nome do restaurante
    restaurante_encontrado = False

    for buscando in restaurantes:
        if nome_restaurante == buscando['nome']:
            restaurante_encontrado = True
            buscando['ativo'] = not buscando['ativo'] #Altera o valor que esta dentro e o inverte
            mensagem = f'O restaurante foi {nome_restaurante} foi ativado com sucesso' if buscando['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem) # esse tipo de mensagem de forma Ternario

    if not restaurante_encontrado:
        print('Restaurante não encontrado')

    volta_ao_menu()

""" TRY

try:
    codigo

except:
    codigo

significa tente, utilixamos isso para que o sistema nao mostre aql mensagem de erro em determinamos pontos
no nosso caso usamos para nao mostrar o erro quando inserimos um valor "a"(str)

"""
def escolher_opcoes():
    try: # tente
        opcao_escolhida = int(input('Escolha uma opção: ')) #sem o int no inicio faz com que o programa interprete tudo que entre como "str"
        # print(f'Você escolheu a opção {opcap_escolhida}.') # interpolação, usando o "f" antes das aspas

        if opcao_escolhida == 1:
            cadastrar_nova_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alterar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    
    except: # caso nao de
        opcao_invalida()


""" FUNÇÃO

função é um bloco de codigo que ira fazer uma determina ação
"""
def main():
     os.system('cls') # essa função limpa o terminal
     exibir_nome_do_programa()
     exibir_opcoes()
     escolher_opcoes()

if __name__ == '__main__': 
    main()

""" EXPLICAÇÃO

Toda vez que o programa é iniciado ele vem com um nome padrão chamado main e utilizando essa função ele 
verifica se o nome do programa realmente é main e exeguta uma função chamada main(), que puxa outra funções.
Então sempre que iniciamos o programa essa outras funções são iniciadas no terminal também.
"""
