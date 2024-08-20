class Pessoa:
    
    def __init__(self,nome='', idade=0, profissao=''):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.title()


    def __str__(self):
        return f'Nome: {self._nome.ljust(20)} | Idade: {str(self._idade).ljust(20)} | Profssão: {self._profissao.ljust(20)} '


    def aniversario(self):
        self._idade =+ 1

    def saudacao(self):
        mensagens = {
            "programador" : "Olá, Programador! Pronto para arrumar os BUGS hoje?"
        }

        return mensagens.get(self._profissao.lower(), "Olá! Que seu dia seja produtivo e cheio de conquistas!")
        


joao = Pessoa('joao', 19, 'Programador')
joao.aniversario()

print(joao)
print(saudacao())