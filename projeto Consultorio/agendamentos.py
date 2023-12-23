from pessoa import Pessoa, Paciente, ProfissionalSaude

class Agendamentos:
    def __init__(self, profissional_saude, paciente, data, hora):
        self.__profissional_saude = profissional_saude
        self.__paciente = paciente
        self.__data = data
        self.__hora = hora

    @property
    def profissional_saude(self):
        return self._profissional_saude

    @profissional_saude.setter
    def profissional_saude(self, novo_profissional_saude):
        self._profissional_saude = novo_profissional_saude

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, novo_paciente):
        self._paciente = novo_paciente

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, nova_data):
        self._data = nova_data
