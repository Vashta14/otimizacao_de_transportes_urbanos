def salvar_saida(nome_arquivo, metodo, caminho, peso_total, solucao_otima, tempo_gasto):
    with open(nome_arquivo, "a") as arquivo: 
        arquivo.write(f"{metodo}:\n")
        #arquivo.write(f"Caminho: {caminho}\n")
        arquivo.write(f"Solucao inicial: {peso_total}\n")
        arquivo.write(f"Solucao final: {solucao_otima}\n")
        desvio_percentual = ((solucao_otima - peso_total) / solucao_otima) * 100
        arquivo.write(f"Desvio percentual: {desvio_percentual}%\n")
        arquivo.write(f"Tempo de execucao: {tempo_gasto:.6f} segundos\n")
        arquivo.write("\n")  