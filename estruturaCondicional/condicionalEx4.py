"""
- Escreva um programa que sempre escolhe o menor caminho a ser percorrido pelo usuário em
função do local onde se encontra e as opções de caminho a serem seguidas. O usuário sempre
parte do ponto A. O usuário deverá fornecer os valores de distância entre os pontos e o programa
deverá apresentar o caminho a ser percorrido e a distância, conforme o exemplo. Sua solução
deve utilizar apenas estruturas condicionais.
"""
b = int(input("Digite a distancia de B: "))
c = int(input("Digite a distancia de C: "))
caminho_percorrido = "A"
distancia_percorrida = 0

if ( b < c ):
    caminho_percorrido += " → B"
    distancia_percorrida += b
    d = int(input("Digite a distancia de D: "))
    e = int(input("Digite a distancia de E: "))
    if ( d < e ):
        caminho_percorrido += " → D"
        distancia_percorrida += d
    
    elif ( e < d ):
        caminho_percorrido += " → E" 
        distancia_percorrida += e

if ( c < b ):
    caminho_percorrido += " → C"
    distancia_percorrida += c
    f = int(input("Digite a distancia de F: "))
    g = int(input("Digite a distancia de G: "))
    if ( f < g ):
        caminho_percorrido += " → F"
        distancia_percorrida += f
    elif ( g < f ):
        caminho_percorrido += " → G" 
        distancia_percorrida += g
print(f"Caminho percorrido: {caminho_percorrido}")
print(f"Distância percorrida: {distancia_percorrida}")
