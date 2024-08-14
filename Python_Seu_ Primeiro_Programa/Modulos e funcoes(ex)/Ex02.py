"""
2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
"""

from time import sleep
def idade():

    condicao = 1
    print('Digite "sair" para sair')
    while condicao == 1:
        idade = int(input('Qual sua idade: '))

        if idade >= 0 and idade <= 12:
            print('Criança')
        
        elif idade >= 13  and idade <= 18:
            print('Adolescente')
        
        elif idade > 18:
            print('Adulto')
        else:
            print('Idade invalida')
            condicao = 0
        close = input('Aperte "ENTER" para verificar uma nova idade: ')
        close.lower()
        if close == 'sair':
            print('Saindo...')
            sleep(1)
            condicao = 0

        

        

    
idade()