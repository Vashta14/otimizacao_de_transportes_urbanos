from leitor_de_arquivo import gerar_matriz_de_adjacencia
from gerador_de_mst import gerar_mst
from gerador_de_ciclos_eulerianos import adicionar_arestas_para_grau_par_otimizado, tsp_guloso

solucao_otima = 50801

def mst(matriz):
    print("mst")
    mst = gerar_mst(matriz)
    ciclo_euleriano_emparelhamento_minimo = adicionar_arestas_para_grau_par_otimizado(matriz, mst)
    peso_eemparelhamento_minimo = 0
    for _u, _v, peso in ciclo_euleriano_emparelhamento_minimo:
        peso_eemparelhamento_minimo += peso
    print(f"Peso ciclo euleriano emparelhamento minimo: {peso_eemparelhamento_minimo}")
    print(f"""Solução inicial: {peso_eemparelhamento_minimo}
Solução final: {solucao_otima}
Desvio percentual: {((solucao_otima - peso_eemparelhamento_minimo) / solucao_otima) * 100}%
""")
    
def guloso(matriz):
    print("guloso")
    caminho, peso_total = tsp_guloso(matriz)
    print(f"""Solução inicial: {peso_total}
Solução final: {solucao_otima}
Desvio percentual: {((solucao_otima - peso_total) / solucao_otima) * 100}%
""")



def main(): 
    matriz = gerar_matriz_de_adjacencia() 
    guloso(matriz)
    mst(matriz)
    
main()