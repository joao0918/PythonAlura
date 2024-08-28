from modelos.restaurante import Resturante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Resturante('praca', 'Gurmet')
sobremesa_pudin = Sobremesa('Pudim', 4.25, 'Gelatina', 'Pequeno', 'O melhor da cidade toda')
bebida_suca = Bebida('Suco de Melancia', 5.00, 'grande')
bebida_suca.aplicar_desconto()
prato_pao = Prato('Pao', 2.00, 'O melhor pao da cidade')
prato_pao.aplicar_desconto()


restaurante_praca.adicionar_no_cardapio(bebida_suca)
restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudin)
def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()