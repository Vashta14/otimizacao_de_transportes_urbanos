import argparse
import time

from leitor_de_arquivo import gerar_matriz_de_adjacencia
from gerador_de_mst import gerar_mst
from gerador_de_ciclos_eulerianos import adicionar_arestas_para_grau_par_otimizado, tsp_guloso
from algoritmo_fleury import converter_para_lista_adjacencia, fleury
from saida import salvar_saida

def mst(matriz):
    inicio = time.time()
    print("mst + emparelhamento perfeito minimo + fleury")
    mst = gerar_mst(matriz)
    ciclo_euleriano_emparelhamento_minimo = adicionar_arestas_para_grau_par_otimizado(matriz, mst)
    caminho = fleury(converter_para_lista_adjacencia(ciclo_euleriano_emparelhamento_minimo, len(matriz) ), 0)
    peso_emparelhamento_minimo = 0
    for _u, _v, peso in ciclo_euleriano_emparelhamento_minimo:
        peso_emparelhamento_minimo += peso
    final = time.time()
    print(f"Solução final: {peso_emparelhamento_minimo}") 
    print(f"Tempo de execução: {final - inicio:.6f} segundos")
    return "mst", caminho, peso_emparelhamento_minimo
    
def guloso(matriz):
    inicio = time.time()
    print("guloso")
    caminho, peso_total = tsp_guloso(matriz)
    final = time.time()
    print(f"Solução final: {peso_total}") 
    print(f"Tempo de execução: {final - inicio:.6f} segundos")
   
    return "guloso",caminho, peso_total



def main(): 
    inicio = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('arquivo', type=str)
    parser.add_argument('solucao_otima', type=int, nargs='?', default=None)
    args = parser.parse_args()

    solucao_otima = args.solucao_otima
    nome_arquivo = args.arquivo
    
    matriz = gerar_matriz_de_adjacencia() 
    guloso_resultado =  guloso(matriz)
    mst_resultado = mst(matriz)
    
    melhor_resultado = guloso_resultado if guloso_resultado[2] < mst_resultado[2] else mst_resultado
    final = time.time()
    salvar_saida(nome_arquivo, melhor_resultado[0], melhor_resultado[1], melhor_resultado[2], solucao_otima, final - inicio)
    
main()