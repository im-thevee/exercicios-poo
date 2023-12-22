from datetime import datetime

def validar_cpf(func):
    def wrapper(self, value):
        if len(value) != 11:
            raise ValueError("CPF inválido")
        return func(self, value)
    return wrapper

class Pessoa:
    def __init__(self, nome, cpf, data_nascimento, sexo):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._sexo = sexo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self._data_nascimento = value

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        self._sexo = value

class Paciente(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, sexo, altura, peso):
        super().__init__(nome, cpf, data_nascimento, sexo)
        self._altura = altura
        self._peso = peso

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, value):
        self._altura = value

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, value):
        self._peso = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    @validar_cpf
    def cpf(self, value):
        self._cpf = value

class ProfissionalSaude(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, sexo, crm):
        super().__init__(nome, cpf, data_nascimento, sexo)
        self._crm = crm

    @property
    def crm(self):
        return self._crm

    @crm.setter
    def crm(self, value):
        self._crm = value

# Exemplo de Uso
paciente1 = Paciente("Maria", "12345678900", "1990-05-15", "Feminino", 165, 55)
print(paciente1.cpf)  # Obtendo o CPF
paciente1.cpf = "12345"  # Tentativa de definir um CPF inválido
