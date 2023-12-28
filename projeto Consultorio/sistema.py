from agendamento import Agendamento, Pessoa, Paciente, ProfissionalSaude

class Sistema:
    def __init__(self):
        self.__lista_profissionais_saude = [
                                            ProfissionalSaude('Antonio Higor', '023.294.230-21', '01/07/1990', 'Masculino', '12124'),
                                            ProfissionalSaude('Samuel Marques', '022.294.017-21', '20/05/1998', 'Masculino', '42315')
                                            ]
        self.__lista_pacientes = [
                            Paciente('Davi Oliveira', '016.708.034-32', '02/04/2001', 'Masculino', '1,80m', '87kg'),
                            Paciente('Marcos Ribeiro', '113.508.034-12', '13/09/1999', 'Masculino', '1,78m', '73kg'),
                            Paciente('José Augusto', '012.212.403-50', '09/08/2005', 'Masculino', '1,67', '80kg')
                            ]
        self.__lista_consultas = [
                                    Agendamento(self.__lista_profissionais_saude[0], self.__lista_pacientes[2], '04/09/2023', '14:00'),
                                    Agendamento(self.__lista_profissionais_saude[0], self.__lista_pacientes[0], '04/09/2023', '14:00'),
                                    Agendamento(self.__lista_profissionais_saude[1], self.__lista_pacientes[0], '02/12/2023', '13:00')
                                ]
    
    def adicionar_paciente(self, paciente: Paciente):
        self.__pacientes.append(paciente)

    def adicionar_profissional_saude(self, profissional: ProfissionalSaude):
        self.__profissionais_saude.append(profissional)

    def adicionar_consulta(self, novo_agendamento: Agendamento):
        self.__lista_consultas.append(novo_agendamento)

    def ver_pacientes_cadastrados(self):
        id = 0
        for paciente in self.__lista_pacientes:
            print(f'| ID {id} {paciente}')
            id += 1

    def ver_profissionais_cadastrados(self):
        id = 0
        for profissional in self.__lista_profissionais_saude:
            print(f'| ID {id} {profissional}')
            id += 1

    def ver_consultas_cadastradas(self):
        id = 0
        for consulta in self.__lista_consultas:
            print(f'| ID {id} {consulta}')
            id += 1

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
            escolha = int(input('Digite o ID para mudar o paciente: '))
            paciente_escolhido = self.__lista_pacientes[escolha]
            print('1- Nome')
            print('2- CPF')
            print('3- Data de nascimento')
            print('4- Sexo')
            print('5- Altura')
            print('6- Peso')
            print('7- Sair')
            opcao = int(input(f'Escolha qual informação do paciente {paciente_escolhido.nome} deve ser alterado? '))
            
            if opcao == 1:
                paciente_escolhido.nome = input('Digite o novo nome do paciente: ')
                print(f'Nome alterado para {paciente_escolhido.nome} com sucesso!')
                self.menu_paciente()

            elif opcao == 2:
                paciente_escolhido.cpf = input(f'Digite o novo CPF de {paciente_escolhido.nome}: ')
                print(f'CPF do paciente {paciente_escolhido.nome} foi alterado para {paciente_escolhido.cpf}')
                self.menu_paciente()

            elif opcao == 3:
                paciente_escolhido.data_nascimento = input(f'Digite a nova data de nascimento de {paciente_escolhido.nome}')
                print(f'A data de nascimento de {paciente_escolhido.nome} foi alterada para {paciente_escolhido.data_nascimento}')
                self.menu_paciente()
            
            elif opcao == 4:
                paciente_escolhido.sexo = input(f'Digite o sexo de {paciente_escolhido.nome}: ')
                print(f'O sexo de {paciente_escolhido.nome} foi alterado para {paciente_escolhido.sexo}')
                self.menu_paciente()

            elif opcao == 5:
                paciente_escolhido.altura = input(f'Digite a nova altura de {paciente_escolhido.nome}: ')
                print(f'A altura de {paciente_escolhido.nome} foi alterada para {paciente_escolhido.altura}')
                self.menu_paciente()
            
            elif opcao == 6:
                paciente_escolhido.peso = input(f'Digite a novo peso de {paciente_escolhido.peso}: ')
                print(f'O peso de {paciente_escolhido.nome} foi alterada para {paciente_escolhido.peso}')
                self.menu_paciente()
            
            elif opcao == 7:
                self.menu_inicial()

            else:
                print('Opção invalida, tente um ID existente!')
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
        
        else:
            print('ID invalido, tente alguma das opções abaixo.')
            self.menu_paciente()

    def menu_profissional_saude(self):
        print('1- Cadastrar profissional da saude')
        print('2- Editar profissional')
        print('3- Excluir profissional')
        print('4- Listar profissional')
        print('5- Voltar pro inicio')
        opcao = int(input('Escolha um dos ID acima: '))
        
        if opcao == 1:
            nome = input('Digite o nome do profissional: ')
            cpf = input('Digite o CPF do profissional: ')
            data = input('Digite a data de nascimento do profissional: ')
            sexo = input('Digite o sexo do profissional: ')
            crm = input('Digite o crm do profissional: ')
            profissional = ProfissionalSaude(nome, cpf, data, sexo, crm)
            self.__lista_profissionais_saude.append(profissional)
            print(f'Profissional {profissional.nome} adicionado com sucesso!')
            self.menu_profissional_saude()

        elif opcao == 2:
            self.ver_profissionais_cadastrados()
            escolha = int(input('Digite o ID para mudar o paciente: '))
            profissional_escolhido = self.__lista_profissionais_saude[escolha]
            print('1- Nome')
            print('2- CPF')
            print('3- Data de nascimento')
            print('4- Sexo')
            print('5- CRM')
            print('6- Sair')
            opcao = int(input(f'Escolha qual informação do profissional da saúde {profissional_escolhido.nome} deve ser alterado: '))
            
            if opcao == 1:
                profissional_escolhido.nome = input('Digite o novo nome do profissional: ')
                print(f'Nome alterado para {profissional_escolhido.nome} com sucesso!')
                self.menu_profissional_saude()

            elif opcao == 2:
                profissional_escolhido.cpf = input(f'Digite o novo CPF de {profissional_escolhido.nome}: ')
                print(f'CPF do profissional {profissional_escolhido.nome} foi alterado para {profissional_escolhido.cpf}')
                self.menu_profissional_saude()

            elif opcao == 3:
                profissional_escolhido.data_nascimento = input(f'Digite a nova data de nascimento de {profissional_escolhido.nome}')
                print(f'A data de nascimento de {profissional_escolhido.nome} foi alterada para {profissional_escolhido.data_nascimento}')
                self.menu_profissional_saude()
            
            elif opcao == 4:
                profissional_escolhido.sexo = input(f'Digite o sexo de {profissional_escolhido.nome}: ')
                print(f'O sexo de {profissional_escolhido.nome} foi alterado para {profissional_escolhido.sexo}')
                self.menu_profissional_saude()

            elif opcao == 5:
                profissional_escolhido.altura = input(f'Digite a nova altura de {profissional_escolhido.nome}: ')
                print(f'A altura de {profissional_escolhido.nome} foi alterada para {profissional_escolhido.altura}')
                self.menu_profissional_saude()
            
            elif opcao == 6:
                profissional_escolhido.crm = input(f'Digite a novo CRM de {profissional_escolhido.crm}: ')
                print(f'O peso de {profissional_escolhido.nome} foi alterada para {profissional_escolhido.crm}')
                self.menu_profissional_saude()
            
            elif opcao == 7:
                self.menu_inicial()

            else:
                print('Opção invalida, tente um ID existente!')
                self.menu_paciente()
                
        elif opcao == 3:
            self.ver_profissionais_cadastrados()
            escolha = int(input('Digite o ID para excluir um paciente: '))
            profissional_escolhido = self.__lista_profissionais_saude[escolha]
            confirmacao = int(input(f'Tem certeza que deseja excluir o profissional {profissional_escolhido.nome}? Digite 1 para sim 2 para não: '))
            
            if confirmacao == 1:
                del self.__lista_profissionais_saude[escolha]
                print(f'Profissional {profissional_escolhido.nome} removido!')
                self.menu_profissional_saude()
            else:
                self.menu_profissional_saude()

        elif opcao == 4:
            self.ver_profissionais_cadastrados()
            self.menu_profissional_saude()

        elif opcao == 5:
            self.menu_inicial()
        
        else:
            print('ID invalido, tente alguma das opções abaixo.')
            self.menu_paciente()

    def menu_agendamento(self):
        print('1- Agendar consulta')
        print('2- Editar consulta')
        print('3- Excluir consulta')
        print('4- Listar consultas')
        opcao = int(input('Escolha um dos ID acima: '))

        if opcao == 1:
            nova_data = input('Digite a data da consulta: ')
            nova_hora = input('Digite a hora da consulta: ')
            
            # Escolhendo um paciente
            while True:
                self.ver_profissionais_cadastrados()
                escolha = int(input('Digite o ID do profissional da saúde para o agendamento: '))
                profissional_escolhido = self.__lista_profissionais_saude[escolha]
                
                for agendamento in self.__lista_consultas:
                    if agendamento.data == nova_data:
                        if agendamento.hora == nova_hora:
                            if agendamento.profissional_saude == profissional_escolhido:
                                print(f'O profissional {agendamento.profissional_saude.nome} já possui agendamento nesse horario!')

                    else:
                        return False  

            self.ver_pacientes_cadastrados()
            escolha = int(input('Digite o ID do profissional da saúde para o agendamento: '))
            paciente_escolhido = self.__lista_pacientes[escolha]
            

        elif opcao == 2:
            pass

        elif opcao == 3:
            pass

        elif opcao == 4:
            self.ver_consultas_cadastradas()
            self.menu_agendamento()

    def menu_inicial(self):
        print('1- Área do Paciente')
        print('2- Área do profissional da saúde')
        print('3- Agendamentos')
        escolha = int(input('Digite a opção deseja de acordo com o ID: '))
        if escolha == 1:
            self.menu_paciente()

        elif escolha == 2:
            self.menu_profissional_saude()
        
        elif escolha == 3:
            self.menu_agendamento()

        else:
            print('Código inválido!')
            self.menu_inicial()
    