# Otimizacao_de_transportes_urbanos

Este projeto implementa uma solucao para o problema de otimizacao das rotas de onibus usando **Árvore Geradora Mínima (MST)** e **Algoritmo Guloso**.

## 📌 Estrutura do Codigo
O codigo esta modularizado nos seguintes arquivos:

- **`leitor_de_arquivo.py`** → Lê o arquivo de entrada e gera a matriz adjacencia.
- **`gerador_de_mst.py`** → Gera a Arvore Geradora Minima (MST), que contem as arestas (u, v, peso) que conectam todos os vertices com o menor custo possivel.
- **`gerador_de_ciclos_eulerianos.py`** → Adiciona arestas, para garantir que tenham grau par e encontra ciclos Eulerianos.
- **`algoritmo_fleury.py`** → Implementa o Algoritmo de Fleury para encontrar o ciclo Euleriano, adicionando e removendo arestas quando necessario. Na implementação convertemos a matriz por lista de adjacencia.
- **`salvar_saida.py`** → Função responsável por salvar os resultados no arquivo de saída.
- **`main.py`** → Organizamos para chamar as funcoes e executar os algoritmos de MST e Guloso.


## Exemplo de uso

- Rode o comando `python ./src/main.py < ./ins/03.ins` no cmd

## Guia de soluções otimas

- 02.ins -> 50801
- 03.ins -> 62128
- 04.ins -> [79952, 80450]
- 05.ins -> 20127
- 06.ins -> [22204, 22249]
- 07.ins -> 56638
- 08.ins -> 56892
- 09.ins -> 8806
- 10.ins -> 57201
