"""
■ Escreva um programa que leia dois valores que representem o início
e o fim de um intervalo. O programa deverá ler um terceiro valor
digitado e verificar se este terceiro valor está dentro do intervalo ou
fora. Caso esteja fora do intervalo, deverá informar se está na parte
inferior ou superior do intervalo.
"""
inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
valor = int(input("Digite um valor: "))

if valor > inicio and valor < fim:
  print("o valor está dentro do intervalo.")
else:
  print("O valor tá fora do intervalo")