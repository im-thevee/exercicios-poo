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
        self.__altura = altura
        self.__peso = peso

    def __str__(self) -> str:
        return f'| Nome : {self._nome} | CPF: {self._cpf} | Data: {self._data_nascimento} | Sexo: {self._sexo} | Altura: {self.__altura} | Peso: {self.__peso} |'

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        self.__altura = value

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, value):
        self.__peso = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

class ProfissionalSaude(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, sexo, crm):
        super().__init__(nome, cpf, data_nascimento, sexo)
        self.__crm = crm

    @property
    def crm(self):
        return self.__crm

    @crm.setter
    def crm(self, value):
        self.__crm = value

