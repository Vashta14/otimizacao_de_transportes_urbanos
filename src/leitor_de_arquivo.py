import sys
import math


# Função que lê o arquivo de entrada e retorna uma lista de tuplas com as coordenadas dos pontos
def ler_arquivo_ins():
    linhas = sys.stdin.readlines()
    
    # Encontrar a seção NODE_COORD_SECTION
    inicio_secao = linhas.index('NODE_COORD_SECTION\n') + 1
    coordenadas = []
    
    for linha in linhas[inicio_secao:]:
        if linha.strip() == 'EOF':
            break
        partes = linha.split()
        # A primeira parte é o index da cidade, as outras duas são as coordenadas x e y
        coordenadas.append((int(partes[0]), float(partes[1]), float(partes[2])))
        
    return coordenadas

# Função que calcula a distância euclidiana entre dois pontos
def calcular_distancia_euclidiana(coord1, coord2):
    xd = coord1[1] - coord2[1]
    yd = coord1[2] - coord2[2]
    return round(math.sqrt(xd * xd + yd * yd))

# Função que preenche a matriz de adjacência com as distâncias euclidianas entre os pontos
def preencher_matriz_adjacencia(coordenadas):
    n = len(coordenadas)
    matriz_adjacencia = [[0] * n for _ in range(n)]
    
    # Preenche a matriz de ajacência criando um grafo completo com as distâncias euclidianas
    for i in range(n):
        for j in range(n):
            if i != j:
                matriz_adjacencia[i][j] = calcular_distancia_euclidiana(coordenadas[i], coordenadas[j])
    
    return matriz_adjacencia

# Função que gera a matriz de adjacência a partir do arquivo de entrada
def gerar_matriz_de_adjacencia():
    coordenadas = ler_arquivo_ins()
    matriz_adjacencia = preencher_matriz_adjacencia(coordenadas)
    
    # print("Matriz de Adjacência:")
    # Imprime a matriz de adjacência
    """
    for linha in range(len(matriz_adjacencia)): 
        for coluna in range(len(matriz_adjacencia[linha])):
            print(str(linha) + ' ' + str(coluna) + ' '+ str(matriz_adjacencia[linha][coluna]) +  ' ')
        print('\n')
    """
    return matriz_adjacencia

