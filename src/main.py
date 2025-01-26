from leitor_de_arquivo import gerar_matriz_de_adjacencia
from gerador_de_mst import gerar_mst
from gerador_de_ciclos_eulerianos import ligar_vertices_impares, adicionar_arestas_para_grau_par_otimizado
from algoritmo_fleury import converter_para_lista_adjacencia, fleury

def main():
    matriz = gerar_matriz_de_adjacencia()
    mst = gerar_mst(matriz)
    ciclo_euleriano_simples = ligar_vertices_impares(matriz, mst)
    ciclo_euleriano_emparelhamento_minimo = adicionar_arestas_para_grau_par_otimizado(matriz, mst)

    grafo_euleriano = adicionar_arestas_para_grau_par_otimizado(matriz, mst)
    n = len(matriz)
    grafo_adj = converter_para_lista_adjacencia(grafo_euleriano, n)
    print("Lista de adjacência do grafo:")
    for u, vizinhos in enumerate(grafo_adj):
        print(f"{u}: {vizinhos}")
        
    inicio = 0
    ciclo_euleriano = fleury(grafo_adj, inicio)
    print(f"Ciclo Euleriano: {ciclo_euleriano}")

    peso_total = 0
    for _u, _v, peso in mst:
        peso_total += peso
    print(f"Peso mst: {peso_total}")
    peso_total = 0
    for _u, _v, peso in ciclo_euleriano_simples:
        peso_total += peso
    print(f"Peso ciclo euleriano simples: {peso_total}")
    peso_total = 0
    for _u, _v, peso in ciclo_euleriano_emparelhamento_minimo:
        peso_total += peso
    print(f"Peso ciclo euleriano emparelhamento minimo: {peso_total}")

main()