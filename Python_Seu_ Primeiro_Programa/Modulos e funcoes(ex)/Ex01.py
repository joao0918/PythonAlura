"""
1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
"""
def par_ou_impar():
    condicao = 1
    while condicao == 1:
        num = int(input('Digite um numero: '))

        if num % 2 == 0:
            print(f'O numero {num} é par')

        else:
            print(f'O numero {num} é impar')
        
        close = str(input('Deseja finalzar o porgrama(sim ou nao)? '))
        close.lower()
        if close == 'sim':
            condicao = 0

par_ou_impar() 