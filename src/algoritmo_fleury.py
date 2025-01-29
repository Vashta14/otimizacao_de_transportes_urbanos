from collections import defaultdict

def eh_ponte(u, v, grafo):
    componentes_originais = contar_componentes_conexos(grafo)
    remover_aresta(grafo, u, v)
    componentes_novos = contar_componentes_conexos(grafo)
    adicionar_aresta(grafo, u, v)
    return componentes_novos > componentes_originais

def contar_componentes_conexos(grafo):
    visitados = set()
    componentes = 0

    def bfs(no):
        fila = [no]
        while fila:
            atual = fila.pop(0)
            for vizinho in grafo[atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

    for no in grafo:
        if no not in visitados:
            componentes += 1
            bfs(no)
    return componentes

def remover_aresta(grafo, u, v):
    if v in grafo[u]:
        grafo[u].remove(v)
    if u in grafo[v]:
        grafo[v].remove(u)

def adicionar_aresta(grafo, u, v):
    grafo[u].append(v)
    grafo[v].append(u)

def fleury(grafo, inicio):
    caminho = [] 
    atual = inicio

    while any(grafo.values()):
        encontrou_aresta_valida = False  

        for vizinho in grafo[atual]:
            if not eh_ponte(atual, vizinho, grafo): 
                caminho.append(atual)
                remover_aresta(grafo, atual, vizinho)
                atual = vizinho
                encontrou_aresta_valida = True
                break

        if not encontrou_aresta_valida:
            if grafo[atual]: 
                vizinho = grafo[atual][0]
                caminho.append(atual)
                remover_aresta(grafo, atual, vizinho)
                atual = vizinho
            else:
                break

    return caminho

def converter_para_lista_adjacencia(grafo, n):
    adj = {i: [] for i in range(n)}
    for u, v, peso in grafo:
        adj[u].append(v)
        adj[v].append(u)
    return adj