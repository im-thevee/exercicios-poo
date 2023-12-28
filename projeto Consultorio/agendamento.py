from pessoa import Pessoa, Paciente, ProfissionalSaude

class Agendamento:
    def __init__(self, profissional_saude: ProfissionalSaude, paciente: Paciente, data, hora):
        self.__profissional_saude = profissional_saude
        self.__paciente = paciente
        self.__data = data
        self.__hora = hora

    def __str__(self) -> str:
        return f'| Profissional da saúde: {self.__profissional_saude.nome} | Paciente: {self.__paciente.nome} | Data: {self.__data} às {self.__hora} horas'

    @property
    def profissional_saude(self):
        return self._profissional_saude

    @profissional_saude.setter
    def profissional_saude(self, novo_profissional_saude):
        self._profissional_saude = novo_profissional_saude

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, novo_paciente):
        self.__paciente = novo_paciente

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, nova_data):
        self.__data = nova_data

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, nova_hora):
        self.__data = nova_hora
