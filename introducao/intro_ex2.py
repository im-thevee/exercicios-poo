"""
■ Escreva um programa para solicitar dois valores inteiros (A e B) ao usuário. Em
seguida exiba as seguintes saída:
■ A > B = [resultado]
■ A <= B = [resultado]
■ A != B = [resultado]
■ A == B = [resultado]
"""
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
print(f"{a} é maior que {b}? {a > b}")
print(f"{a} é menor igual a {b}? {a <= b}")
print(f"{a} é diferente de {b}? {a != b}")
print(f"{a} é igual a {b}? {a == b}")
