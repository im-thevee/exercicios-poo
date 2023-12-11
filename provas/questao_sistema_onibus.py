class Motorista:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.lista_onibus = []

    def __str__(self):
        return f"| Motorista: {self.nome} | CPF: {self.cpf} |"

    def listar_onibus(self):
        return self.lista_onibus

class Onibus:
    def __init__(self, nome, numero, placa):
        self.nome = nome
        self.numero = numero
        self.placa = placa
        self.motoristas = []

    def __str__(self):
        return f"| Ônibus: {self.nome} | Número: {self.numero} | Placa: {self.placa} |"

    def listar_motoristas(self):
        return self.motoristas


class Sistema:
    def __init__(self):
        self.motoristas = [Motorista('Higor o Home', '1'),
                           Motorista('Davi', '2'),
                           Motorista('Augusto', '3'),
                           Motorista('Marcola', '4')
                           ]
        self.onibus = [Onibus('Vale Do Sol', 'V', 'XMML3453'),
                       Onibus('Cidade Verde', '399', 'PY3984')]

    def cadastrar_motorista(self, cpf, nome):
        novo_motorista = Motorista(cpf, nome)
        self.motoristas.append(novo_motorista)
        return novo_motorista

    def cadastrar_onibus(self, nome, numero, placa):
        novo_onibus = Onibus(nome, numero, placa)
        self.onibus.append(novo_onibus)
        return novo_onibus

    def listar_motoristas(self):
        return self.motoristas

    def listar_onibus(self):
        return self.onibus

    def vincular_motorista_onibus(self, motorista, onibus):
        if motorista not in onibus.motoristas:
            onibus.motoristas.append(motorista)
        if onibus not in motorista.lista_onibus:
            motorista.lista_onibus.append(onibus)

    def vincular_onibus_motorista(self, onibus, motorista):
        self.vincular_motorista_onibus(motorista, onibus)

    def listar_motoristas_por_onibus(self, numero):
        for onibus in self.onibus:
            if onibus.numero == numero:
                return onibus.listar_motoristas()
        return None

    def listar_onibus_por_motorista(self, cpf):
        for motorista in self.motoristas:
            if motorista.cpf == cpf:
                return motorista.listar_onibus()
        return None

    def menu(self):
        while True:
            print("\n ---- | Rodoviaria do Biquine | ---- ")
            print("| ID 1 | Cadastrar Motorista")
            print("| ID 2 | Cadastrar Ônibus")
            print("| ID 3 | Ver lista de Motoristas")
            print("| ID 4 | Ver lista de Ônibus")
            print("| ID 5 | Vincular Motorista a Ônibus")
            print("| ID 6 | Vincular Ônibus a Motorista")
            print("| ID 7 | Ver lista de Motoristas por Ônibus")
            print("| ID 8 | Ver lista de Ônibus por Motorista")
            print("| ID 0 | Sair")

            escolha = input("Escolha um dos ID acima para continuar: ")

            if escolha == "1":
                cpf = input("Digite o CPF do motorista: ")
                nome = input("Digite o nome do motorista: ")
                self.cadastrar_motorista(cpf, nome)
                print("Motorista cadastrado com sucesso!")

            elif escolha == "2":
                nome = input("Digite o nome do ônibus: ")
                numero = input("Digite o número do ônibus: ")
                placa = input("Digite a placa do ônibus: ")
                self.cadastrar_onibus(nome, numero, placa)
                print("Ônibus cadastrado com sucesso!")

            elif escolha == "3":
                print("\nLista de Motoristas:")
                for motorista in self.listar_motoristas():
                    print(motorista)

            elif escolha == "4":
                print("\nLista de Ônibus:")
                for onibus in self.listar_onibus():
                    print(onibus)

            elif escolha == "5":
                cpf = input("Digite o CPF do motorista: ")
                numero = input("Digite o número do ônibus: ")

                motorista_encontrado = None
                onibus_encontrado = None

                for motorista in self.listar_motoristas():
                    if motorista.cpf == cpf:
                        motorista_encontrado = motorista
                        break

                for onibus in self.listar_onibus():
                    if onibus.numero == numero:
                        onibus_encontrado = onibus
                        break

                if motorista_encontrado and onibus_encontrado:
                    self.vincular_motorista_onibus(motorista_encontrado, onibus_encontrado)
                    print(f"O motorista {motorista_encontrado.nome} foi vinculado ao ônibus {onibus_encontrado.nome} {onibus_encontrado.numero}")
                else:
                    print("Motorista ou ônibus não encontrados.")

            elif escolha == "6":
                numero = input("Digite o número do ônibus: ")
                cpf = input("Digite o CPF do motorista: ")

                onibus_encontrado = None
                motorista_encontrado = None

                for onibus in self.listar_onibus():
                    if onibus.numero == numero:
                        onibus_encontrado = onibus
                        break

                for motorista in self.listar_motoristas():
                    if motorista.cpf == cpf:
                        motorista_encontrado = motorista
                        break

                if onibus_encontrado and motorista_encontrado:
                    self.vincular_onibus_motorista(onibus_encontrado, motorista_encontrado)
                    print(f"Ônibus {onibus_encontrado.nome} {onibus_encontrado.numero} foi vinculado ao motorista {motorista_encontrado.nome}")
                else:
                    print("Ônibus ou motorista não encontrados.")

            elif escolha == "7":
                numero = input("Digite o número do ônibus: ")

                onibus_encontrado = None

                for onibus in self.listar_onibus():
                    if onibus.numero == numero:
                        onibus_encontrado = onibus
                        break

                if onibus_encontrado:
                    motoristas = onibus_encontrado.listar_motoristas()
                    if motoristas:
                        print(f"\nMotoristas vinculados ao ônibus {onibus_encontrado.numero}:")
                        for motorista in motoristas:
                            print(motorista)
                    else:
                        print("Não há motoristas vinculados a este ônibus.")
                else:
                    print("Ônibus não encontrado.")

            elif escolha == "8":
                cpf = input("Digite o CPF do motorista: ")

                motorista_encontrado = None

                for motorista in self.listar_motoristas():
                    if motorista.cpf == cpf:
                        motorista_encontrado = motorista
                        break

                if motorista_encontrado:
                    onibus = motorista_encontrado.listar_onibus()
                    if onibus:
                        print(f"\nÔnibus vinculados ao motorista {motorista}")

sistema = Sistema()
sistema.menu()