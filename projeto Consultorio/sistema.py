from agendamentos import Agendamentos, Pessoa, Paciente, ProfissionalSaude

class Sistema:
    def __init__(self):
        self.__lista_consultas = []
        self.__lista_profissionais_saude = []
        self.__lista_pacientes = [
                            Paciente('Davi Oliveira', '016708034-32', '02/04/2001', 'Masculino', '1,80m', '77kg'),
                            Paciente('Marcos Ribeiro', '113508034-12', '12/02/1999', 'Masculino', '1,79m', '73kg')
                            ]
    
    def adicionar_paciente(self, paciente: Paciente):
        self.__pacientes.append(paciente)

    def adicionar_profissional_saude(self, profissional: ProfissionalSaude):
        self.__profissionais_saude.append(profissional)

    def ver_pacientes_cadastrados(self):
        id = 0
        for paciente in self.__lista_pacientes:
            print(f'| ID {id} {paciente}')
            id += 1

    def ver_profissionais_cadastrados(self):
        for profissional in self.__lista_profissionais_saude:
            print(profissional.nome)

    def agendar_consulta(self):
        pass

    def menu_paciente(self):
        print('1- Cadastrar paciente')
        print('2- Editar paciente')
        print('3- Excluir Paciente')
        print('4- Listar pacientes')
        print('5- Voltar pro inicio')
        opcao = int(input('Escolha um dos ID acima: '))
        
        if opcao == 1:
            nome = input('Digite o nome do paciente: ')
            cpf = input('Digite o CPF do paciente: ')
            data = input('Digite a data de nascimento do paciente: ')
            sexo = input('Digite o sexo do paciente: ')
            altura = input('Digite a altura do paciente: ')
            peso = input('Digite o peso do paciente: ')
            paciente = Paciente(nome, cpf, data, sexo, altura, peso)
            self.__lista_pacientes.append(paciente)
            print(f'Paciente {paciente.nome} adicionado com sucesso!')
            self.menu_paciente()

        elif opcao == 2:
            self.ver_pacientes_cadastrados()
            escolha = int(input('Digite o ID para mudar o paciente'))
            paciente_escolhido = self.__lista_pacientes[escolha]
            self.menu_paciente()
            
        elif opcao == 3:
            self.ver_pacientes_cadastrados()
            escolha = int(input('Digite o ID para excluir um paciente: '))
            paciente_escolhido = self.__lista_pacientes[escolha]
            confirmacao = int(input(f'Tem certeza que deseja excluir o paciente {paciente_escolhido.nome}? Digite 1 para sim 2 para não: '))
            
            if confirmacao == 1:
                del self.__lista_pacientes[escolha]
                print(f'Paciente {paciente_escolhido.nome} removido!')
                self.menu_inicial()
            else:
                self.menu_paciente()

        elif opcao == 4:
            self.ver_pacientes_cadastrados()
            self.menu_paciente()

        elif opcao == 5:
            self.menu_inicial()

    def menu_inicial(self):
        print('1- Área do Paciente')
        print('2- Área do profissional da saúde')
        print('3- Agendamentos')
        escolha = int(input('Digite a opção deseja de acordo com o ID: '))
        if escolha == 1:
            self.menu_paciente()

        else:
            print('Código inválido!')
            self.menu_inicial()
    