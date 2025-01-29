def salvar_saida(nome_arquivo, metodo, caminho, peso_total, solucao_otima, tempo_gasto):
    print(f"{metodo}:")
    if not nome_arquivo:
        nome_arquivo = "saida.txt"
    
    with open(nome_arquivo, "a") as arquivo: 
        arquivo.write(f"{metodo}:\n")
        arquivo.write(f"Solucao inicial: {peso_total}\n")
        if solucao_otima:
            arquivo.write(f"Solucao final: {solucao_otima}\n")
            desvio_percentual = ((solucao_otima - peso_total) / solucao_otima) * 100
            arquivo.write(f"Desvio percentual: {desvio_percentual:.2f}%\n")
        arquivo.write(f"Tempo de execucao: {tempo_gasto:.6f} segundos\n")
        arquivo.write(f"Caminho: {caminho}\n")
        arquivo.write("\n")  
    print("Resultado salvo em", nome_arquivo)