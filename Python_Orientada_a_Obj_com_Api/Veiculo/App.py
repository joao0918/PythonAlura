from pasta.carro import Carro
from pasta.moto import Moto

carro_baixo = Carro('BMW', "SUV", "4")
moto_corrida = Moto("BMW", "Big Trail", "Esportiva")

def main():
    print(carro_baixo)
    print(moto_corrida)

if __name__ == '__main__':
    main()