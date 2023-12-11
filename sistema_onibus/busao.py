from motorista import Motorista

class Onibus:
    def __init__(self, nome, numero, placa):
        self.nome = nome
        self.numero = numero
        self.placa = placa
        self.lista_motoristas = []
    
    def __str__(self) -> str:
        return f'| Onibus: {self.nome} {self.numero} | Placa: {self.placa}'
    
    def setNome(self, novo_nome_onibus):
        self.nome = novo_nome_onibus

    def getNome(self):
        return self.nome

    def setPlaca(self, nova_placa):
        self.placa = nova_placa
    
    def vincular_motorista(self, motorista: Motorista):
        self.lista_onibus.append(motorista)

