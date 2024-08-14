class Carro:
    
    carros = []
    
    def __init__(self,Cor, Ano):
        
        self.Cor = Cor
        self.Ano = Ano

        Carro.carros.append(self)

    def __str__(self):
        return f'{self.Cor} | {self.Ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.Cor} | {carro.Ano}')
            
kia = Carro('Azul', '2024')

Carro.listar_carros()