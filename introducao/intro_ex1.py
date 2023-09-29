"""
Escreva um programa para solicitar dois valores inteiros (A e B) ao usuário. Em
seguida exiba as seguintes saída:
■ A + B = [resultado]
■ A * B = [resultado]
■ A - B = [resultado]
■ A / B = [resultado]
"""
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
print(f"A soma dos números é igual a {a + b}")
print(f"A subtração do primeiro número pelo segundo é igual a {a - b}")
print(f"O produto dos números é igual a {a * b}")
print(f"A divisão do primeiro número pelo segundo número é igual a {a/b:.2f}")
