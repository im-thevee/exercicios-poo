"""
■ Escreva um programa que sempre escolhe o menor caminho a ser percorrido pelo usuário em
função do local onde se encontra e as opções de caminho a serem seguidas. O usuário sempre
parte do ponto A. O usuário deverá fornecer os valores de distância entre os pontos e o programa
deverá apresentar o caminho a ser percorrido e a distância, conforme o exemplo. Sua solução
deve utilizar apenas estruturas condicionais.
"""
escolhas = ["A"]
b = int(input("Digite a distancia de B: "))
c = int(input("Digite a distancia de C: "))

if ( b < c ):
    escolhas.append(f"B = {b}")
    d = int(input("Digite a distancia de D: "))
    e = int(input("Digite a distancia de E: "))
    if ( d < e ):
        escolhas.append(f"D = {d}")
    elif ( e < d ):
        escolhas.append(f"E = {e}") 
         
if ( c < b ):
    escolhas.append(f"C = {c}")
    f = int(input("Digite a distancia de F: "))
    g = int(input("Digite a distancia de G: "))
    if ( f < g ):
        escolhas.append(f"F = {f}")
    elif ( g < f ):
        escolhas.append(f"G = {g}") 
print(escolhas)