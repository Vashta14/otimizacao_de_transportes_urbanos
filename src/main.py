from leitor_de_arquivo import gerar_matriz_de_adjacencia
from gerador_de_mst import gerar_mst
from gerador_de_ciclos_eulerianos import ligar_vertices_impares, adicionar_arestas_para_grau_par_otimizado

def main():
    matriz = gerar_matriz_de_adjacencia()
    mst = gerar_mst(matriz)
    ciclo_euleriano_simples = ligar_vertices_impares(matriz, mst)
    ciclo_euleriano_emparelhamento_minimo = adicionar_arestas_para_grau_par_otimizado(matriz, mst)
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