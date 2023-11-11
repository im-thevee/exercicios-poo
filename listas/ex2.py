"""
■ Implemente um programa que realiza o cálculo de uma lista de
valores de y correspondente a uma equação de primeiro grau, a
qual é dada por y = a*x + b
■ O programa deverá:
    ■ Perguntar ao usuário quantas equações serão calculadas
    ■ Pergunta os valores de a, b e x para cada uma das equações
    ■ Exibir a equação no forma “y = a*x + b”, substituindo cada 
    valor de a, b e x pelo valores fornecidos pelo próprio usuário
    ■ Exibir o valor de y em cada uma das funções
    ■ Use listas para armazenar os valores das variáveis fornecidos 
    pelo usuário
"""
quant_func_afim = int(input("Quantas equações serão calculadas?"))
lista_resultados = []

for func_afim in range(1, quant_func_afim + 1):
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    x = float(input("Digite o valor de X: "))
    y = a * x + b
    lista_resultados.append(f"Na operação f(x) = {a} x {x} + B, o valor de Y foi de = {y}")

for resposta in lista_resultados:
    print(resposta)

