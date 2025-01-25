def ligar_vertices_impares(matriz_adjacencia, mst):
    n = len(matriz_adjacencia)
    grau = [0] * n
    for u, v, _peso in mst:
        grau[u] += 1
        grau[v] += 1

    arestas_adicionais = []
    for i in range(n):
        for j in range(i + 1, n):
            if grau[i] % 2 != 0 and grau[j] % 2 != 0 and matriz_adjacencia[i][j] != 0:
                arestas_adicionais.append((matriz_adjacencia[i][j], i, j))
                grau[i] += 1
                grau[j] += 1

    grafo_euleriano = mst.copy()

    for peso, u, v in arestas_adicionais:
        grafo_euleriano.append((u, v, peso))

    return grafo_euleriano


def encontrar_vertices_impares(mst, n):
    grau = [0] * n
    for u, v, _peso in mst:
        grau[u] += 1
        grau[v] += 1
    vertices_impares = [i for i in range(n) if grau[i] % 2 != 0]
    return vertices_impares
  
def emparelhamento_perfeito_minimo(vertices_impares, matriz_adjacencia):
    n = len(vertices_impares)
    emparelhamento = []
    visitados = [False] * n

    def encontrar_minimo(i):
        min_peso = float('inf')
        min_j = -1
        for j in range(n):
            if not visitados[j] and i != j:
                peso = matriz_adjacencia[vertices_impares[i]][vertices_impares[j]]
                if peso < min_peso:
                    min_peso = peso
                    min_j = j
        return min_j, min_peso

    for i in range(n):
        if not visitados[i]:
            j, peso = encontrar_minimo(i)
            if j != -1:
                emparelhamento.append((vertices_impares[i], vertices_impares[j], peso))
                visitados[i] = True
                visitados[j] = True

    return emparelhamento

def adicionar_arestas_para_grau_par_otimizado(matriz_adjacencia, mst):
    n = len(matriz_adjacencia)
    vertices_impares = encontrar_vertices_impares(mst, n)
    arestas_adicionais = emparelhamento_perfeito_minimo(vertices_impares, matriz_adjacencia)
    grafo_euleriano = mst.copy()
    for u, v, peso in arestas_adicionais:
        grafo_euleriano.append((u, v, peso))
    return grafo_euleriano