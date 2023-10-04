"""
Escreva um algoritmo que solicite ao usuário um número entre 1 e 10000 e
depois informe para o usuário se o número digitado é primo. Um número é dito
ser primo quando ele é divisível apenas por 1 e ele mesmo.
"""
intervalo = False
divisores = 0
numero = 0
while intervalo == False:
    if numero > 0 and numero < 1000:
        numero = int(input("Digite um número: "))
    divisor = 0
while divisor < numero:
    if numero % divisor == 0:
        divisores += 1

if divisores == 2:
    print("Eh primo")
else:
    print("Não é primo")
