class Cliente:
    def __init__(self, nome, cpf, renda):
        self.__nome = nome
        self.__cpf = cpf
        self.__renda = renda
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def renda(self):
        return self.__renda
    
    @renda.setter
    def renda(self, renda):
        self.__renda = renda

cliente1 = Cliente('Davi', '213.123.423-23', 2000)

print(f"Meu nome é {cliente1.nome}, meu cpf é {cliente1.cpf} e minha renda é de R${cliente1.renda}")
cliente1.nome = 'Leonardo'
cliente1.cpf = '213.412.489-23'
print(f"Meu nome é {cliente1.nome}, meu cpf é {cliente1.cpf} e minha renda é de R${cliente1.renda}")