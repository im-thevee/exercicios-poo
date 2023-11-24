"""
2. Considere a abstração de um objeto cachorro. Crie uma classe
que possa representar as características e ações que podem ser
realizadas por esse objeto. Implemente a classe e um programa
que faça um teste demonstrativo do funcionamento da mesma.
"""
class Cachorro:
  def __init__(self, nome, raca, idade):
    self.nome = nome
    self.raca = raca
    self.idade = idade
  
  def infos(self):
    print(f"Nome: {self.nome} | Idade = {self.idade} | Raça = {self.raca}")

  def latir(self):
    print(f"{self.nome} esta latindo")

  def comer(self):
    print(f"{self.nome} esta comendo")

cachorro1 = Cachorro('Leitica', 'Poodle', '12')
cachorro1.infos()
cachorro1.latir()