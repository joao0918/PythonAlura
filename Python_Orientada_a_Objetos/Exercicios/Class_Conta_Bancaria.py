class ContaBancaria:

    contas = []

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True 