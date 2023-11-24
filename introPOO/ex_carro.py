"""
1. Considere a abstração de um objeto carro. Crie uma classe que
possa representar as características e ações que podem ser
realizadas por esse objeto. Implemente a classe e um programa
que faça um teste demonstrativo do funcionamento da mesma.
"""
class Carro:
  def __init__(self, marca, modelo, cor):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.velocidade = 0

  def aumentarVelocidade(self, velocidade):
    self.velocidade += velocidade

  def reduzirVelocidade(self, reducao):
    if self.velocidade >= reducao:
      self.velocidade -= reducao
    else:
      self.velocidade = 0

  def freitar(self):
    self.velocidade = 0


carro1 = Carro('chevrolet', 'Onix', 'Vermelho')
print(f"Comprei meu primeiro carro da {carro1.marca}, modelo {carro1.modelo}, da cor {carro1.cor}")
carro1.aumentarVelocidade(30)
print(f"Estou atualmente há {carro1.velocidade} KM/h")
