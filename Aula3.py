# PRATICA

list_numbers = [1,2,3,4,5,6,7,8,9,10]
list_names = ['joao', 'pedro', 'aranda', 'moreira']
list_ano = {'Ano Atual': 2024, 'ano de nascimento': 2003}

for numeros in list_ano:
    print(numeros)

for numeros in reversed(list_numbers): # invert the list 
    print(numeros)

lista_de_numeros = []

try:
    while True:
        numero = int(input('Digite um numero: '))

        if numero >= 0:
            lista_de_numeros.append(numero)

        else:
            break
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
media = sum(lista_de_numeros) / len(lista_de_numeros)

print(f'Aqui esta a lista = {lista_de_numeros} e aqui esta a media da soma desses numero = {media:.2f}')