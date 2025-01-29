## Cabecalho

Este e um trabalho da disciplina de Algoritmos em Grafos - GCC218
- Ministrado pelo: Professor Mayron César de Oliveira Moreira.
- Realizado pelos alunos: 
Carlos Eduardo Borges de Sousa - 202020296
Raul Souza Lima -  



# Otimizacao_de_transportes_urbanos

Este projeto implementa uma solucao para o problema de otimizacao das rotas de onibus usando **Árvore Geradora Mínima (MST)** e **Algoritmo Guloso**.



## Estrutura do Codigo
O codigo esta modularizado nos seguintes arquivos:

- **`leitor_de_arquivo.py`** → Lê o arquivo de entrada e gera a matriz adjacencia.
- **`gerador_de_mst.py`** → Gera a Arvore Geradora Minima (MST), que contem as arestas (u, v, peso) que conectam todos os vertices com o menor custo possivel.
- **`gerador_de_ciclos_eulerianos.py`** → Adiciona arestas, para garantir que tenham grau par e encontra ciclos Eulerianos.
- **`algoritmo_fleury.py`** → Implementa o Algoritmo de Fleury para encontrar o ciclo Euleriano, adicionando e removendo arestas quando necessario. Na implementação convertemos a matriz por lista de adjacencia.
- **`salvar_saida.py`** → Função responsável por salvar os resultados no arquivo de saída.
- **`main.py`** → Organizamos para chamar as funcoes e executar os algoritmos de MST e Guloso.


## Funcionamento dos Algoritmos

Guloso:
- Adiciona arestas ao grafo MST para garantir que todos os vertices tenham grau par. 
- Encontra os vertices de grau impar.
- Faz um emparelhamento minimo entre os vertices impares e os marca para nao repetir.
- Otimiza adicionando as menores arestas entre os vertices impares.
- Por fim ele tenta resolver de forma gulosa, começando em um vertice e sempre escolhe o próximo vértice mais próximo ate visitar todos.

MST:
- Verificar se adicionar uma aresta ao grafo criaria um ciclo.
- Depois implementa o Algoritmo de Kruskal para encontrar a Arvore Geradora Minima(MST).
- Utiliza o Algoritmo de Fleury para encontrar o caminho final.

Fleury:
- Converte a representação do grafo de uma matriz de adjacencia para uma lista de adjacencia.
- Verifica se a aresta (u, v) é uma ponte, removendo-a temporariamente.
- Conta o número de componentes conexos no grafo usando Busca em Largura (BFS).
- Manipula a estrutura do grafo, podendo remover ou adicionar arestas.
- Por fim ele percorre todas as arestas e controi o Ciclo Euleriano.


## Entradas

- Os arquivos de entrada sao instancias fornecidas, no formato "02.ins" por exemplo:
1 0.00000e+00 0.00000e+00
2 8.37000e+02 9.58300e+02
3 8.62400e+02 9.58300e+02
4 8.87800e+02 9.58300e+02
5 9.13200e+02 9.58300e+02


## Saida

A saida e feita em um arquivo no formato "saida.txt".
- Fornece o metodo usado.
- Solucao inicial.
- Solucao final.
- Desvio percentual.
- Tempo computacional.

Por exemplo:

Guloso:
Solucao inicial: 74032
Solucao final: 50801
Desvio percentual: -45.729414775299695%
Tempo de execucao: 0.238265 segundos

## Exemplo de uso

- Rode o comando `python ./src/main.py < ./ins/03.ins` no cmd

## Repositorio no GitHub

https://github.com/Vashta14/otimizacao_de_transportes_urbanos.git

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
