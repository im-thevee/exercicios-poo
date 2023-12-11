from busao import Onibus

class Motorista:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.lista_onibus = []

    def __str__(self) -> str:
        return f'| Motorista: {self.nome} | CPF: {self.cpf} |'

    def setNome(self, novo_nome):
        self.nome = novo_nome
    
    def getNome(self):
        return self.nome
    
    def getCpf(self):
        return self.cpf
    
    def vincular_onibus(self, onibus: Onibus):
        self.lista_onibus.append(onibus)

    def exibir_onibus_vinculado(self):
        for onibus in self.lista_onibus:
            print(onibus) 