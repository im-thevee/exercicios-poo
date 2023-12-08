# Crie um jogo de dados que simule uma partida entre dois jogadores. O jogo
# deve possuir três rodadas e cada jogador deve lançar dois dados em cada rodada. O
# jogador que obtiver o maior número de pontos ao final das três rodadas vence o jogo.
# Crie as classes necessárias para resolver o problema.
import random

class Dado:
    def __init__(self):
        self.valorRolagem = 0

    def getValorRolagem(self):
        self.valorRolagem = random.randint(1, 6)
        return self.valorRolagem

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0

    def jogarDado(self, dado: Dado):
        valor_rolagem = dado.getValorRolagem()
        print(f'| Jogador {self.nome} | Rolagem = {valor_rolagem} |')
        self.pontos += valor_rolagem
  
    def getNome(self):
        return self.nome    
  
    def getPontuacao(self): 
        return self.pontos

class Jogo:
    def __init__(self, jogador1: Jogador, jogador2: Jogador):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.rodada = 1

    def jogarRodada(self, dado: Dado):
            print(f'------| Rodada {self.rodada} |------')
            self.jogador1.jogarDado(dado)
            self.jogador2.jogarDado(dado)
            print()
            self.rodada += 1
    
    def acabarJogo(self, dado: Dado):
        if self.jogador1.getPontuacao() > self.jogador2.getPontuacao():
            print(f'{self.jogador1.getNome()} venceu o jogo! Com o placar de {self.jogador1.getPontuacao()} x {self.jogador2.getPontuacao()}')
        
        elif self.jogador2.getPontuacao() > self.jogador1.getPontuacao():
            print(f'{self.jogador2.getNome()} venceu o jogo! Com o placar de {self.jogador2.getPontuacao()} x {self.jogador1.getPontuacao()}')
        
        else:
            print(f'--------- | Os jogadores estão empatados! ({self.jogador1.getPontuacao()} X {self.jogador2.getPontuacao()})| -----------')
            print()
            while self.jogador1.getPontuacao() == self.jogador2.getPontuacao():
                self.jogarRodada(dado)
            
            if self.jogador1.getPontuacao() > self.jogador2.getPontuacao():
                print(f'{self.jogador1.getNome()} venceu o jogo! Com o placar de {self.jogador1.getPontuacao()} x {self.jogador2.getPontuacao()}')
    
            elif self.jogador2.getPontuacao() > self.jogador1.getPontuacao():
                print(f'{self.jogador2.getNome()} venceu o jogo! Com o placar de {self.jogador2.getPontuacao()} x {self.jogador1.getPontuacao()}')
            
    def jogarJogo(self, dado: Dado):
        while self.rodada <= 3:
            self.jogarRodada(dado)
        
        self.acabarJogo(dado)
            
jogador1 = Jogador('Davi')
jogador2 = Jogador('Augusto')
dado = Dado()
jogo = Jogo(jogador1, jogador2)
jogo.jogarJogo(dado)