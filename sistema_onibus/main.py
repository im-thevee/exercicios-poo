from busao import Onibus
from motorista import Motorista

class Sistema:
    def __init__(self):
        self.lista_onibus = [Onibus('Cidade Verde', '399', 'XML219394')]
        self.lista_motoristas = [Motorista('Augusto', '1'), Motorista('Marcola','2'), Motorista('Higor O Cara', '3')]
        
    def adicionar_motorista(self, motorista: Motorista):
        self.lista_motoristas.append(motorista)

    def adicionar_onibus(self, onibus: Onibus):
        self.lista_onibus.append(onibus)
    
    def ver_motoristas_registrados(self):
        print('---------- | Lista De Motoristas | ----------')
        id = 0
        for motorista in self.lista_motoristas:
            print(f'ID: {id} {motorista}')
            id += 1

    def ver_onibus_registrado(self):
        print('---------- | Lista De Onibus | ----------')
        id = 0
        for onibus in self.lista_onibus:
            print(f'ID: {id} {onibus}')
            id += 1

    def cadastrar_onibus(self):
        nome = input('Digite o nome do onibus: ')
        numero = input('Digite o numero do onibus: ')
        placa = input('Digite a placa do onibus')
        novo_onibus = Onibus(nome, numero, placa)
        self.lista_onibus.append(novo_onibus)
        print(f'{novo_onibus} foi adicionado com sucesso!')
        self.voltar_inicio()

    def cadastrar_motorista(self):
        nome = input('Digite o nome do motorista: ')
        cpf = input('Digite o cpf do motorista: ')
        novo_motorista = Motorista(nome, cpf)
        self.lista_motoristas.append(novo_motorista)
        print(f'{novo_motorista} foi adicionado com sucesso!')
        self.voltar_inicio()

    def vincular_motorista_onibus(self):
        print('---------------- | Vincular Motorista | ----------------')
        print('Escolha um dos motoristas abaixo para vincular um onibus.')
        id = 0
        for motorista in self.lista_motoristas:
            print(f'ID: {id} {motorista}')
            id += 1
        
        escolha_motorista = int(input('ID escolhido: '))
        motorista = self.lista_motoristas[escolha_motorista]  
        print('Escolha um onibus para vincular ao motorista.')
        
        id = 0
        for onibus in self.lista_onibus:
            print(f'ID: {id} {onibus}')
            id += 1
        
        escolha_onibus = int(input('ID escolhido: '))
        onibus = self.lista_onibus[escolha_onibus]
        motorista.vincular_onibus(onibus)
        print(f'Motorista {motorista.getNome()} vinculado ao {onibus.getNome()}')
        self.voltar_inicio()
  
    def voltar_inicio(self):
        voltar = int(input('Deseja volta para o menu iniciar?\n1- Sim 2- Não\n'))
        while voltar != 1 or voltar != 2:
            if voltar == 1:
                self.inicio_sistema()
            else:
                print('Sistema Encerrado!')
    
    def inicio_sistema(self):
        print(' -------- | Bem vindo a Frota Theevyus | -------- ')
        print('Escolha uma das opções abaixo para usar nosso sistema\n')
        print('ID 1 - Ver motoristas registrados')
        print('ID 2 - Ver onibus registrados')
        print('ID 3 - Adicionar onibus')
        print('ID 4 - Adicionar motorista')
        print('ID 5 - Vincular motorista a um onibus')
        opcao = int(input('\nOpção escolhida: '))

        if opcao == 1:
            self.ver_motoristas_registrados()
            self.voltar_inicio()
        
        elif opcao == 2: 
            self.ver_onibus_registrado()
            self.voltar_inicio()

        elif opcao == 3:
            self.cadastrar_onibus()
            self.voltar_inicio()
        
        elif opcao == 4:
            self.cadastrar_motorista()
            self.voltar_inicio()
        
        elif opcao == 5:
            self.vincular_motorista_onibus()
            self.voltar_inicio

        else: 
            print('Opcao Invalida')
            self.voltar_inicio()

sistema = Sistema()
sistema.inicio_sistema()