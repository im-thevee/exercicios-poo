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
    
    def getLista(self):
        retorno = 'Motorista Vinculado: '
        for motorista in self.lista_motoristas:
            retorno += motorista.getNome() + " | "
        return retorno
        
    def vincular_motorista(self, motorista):
        self.lista_motoristas.append(motorista)
