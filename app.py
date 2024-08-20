from modelos.restaurante import Resturante
from modelos.avaliacao import Avaliacao

restaurante_praca = Resturante('praca', 'Gourmet')
restaurante_porco = Resturante('joao', 'porco')
restaurante_praca.receber_avaliacao('Joao', 10)
restaurante_praca.receber_avaliacao('lais', 7)
restaurante_praca.receber_avaliacao('lili', 5)

def main():
    Resturante.lista_restaurante()

if __name__ == '__main__':
    main()