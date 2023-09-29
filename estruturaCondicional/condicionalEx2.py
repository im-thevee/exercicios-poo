"""
■ Escreva um algoritmo que solicite que o usuário digite o valor de
duas notas e armazene o resultado em duas variáveis diferentes (tipo
real);

■ Calcule o resultado da média desses valores;

■ Imprima “Você está em RECUPERAÇÃO!!!” caso o resultado da média
seja maior ou igual a 30 e menor do que 70.
"""
notas = input().split(" ")
nota1 = int(notas[0])
nota2 = int(notas[1])

media = (nota1+nota2) / 2

if (media >= 70):
  print(f"Sua média foi de {media:.0f}, você foi aprovado")
elif (media < 70 and media >= 30):
  print(f"Sua média foi de {media:.0f}, você está de recuperação")
else:
  print(f"Sua média foi de {media:.0f}, você foi reprovado")