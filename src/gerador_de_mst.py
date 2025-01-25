class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def gerar_mst(matriz_adjacencia):
    n = len(matriz_adjacencia)
    arestas = []

    # Cria uma lista de arestas com suas respectivas distâncias
    for i in range(n):
        for j in range(i + 1, n):
            if matriz_adjacencia[i][j] != 0:
                arestas.append((matriz_adjacencia[i][j], i, j))

    # Ordena as arestas pelo peso (distância)
    arestas.sort()

    uf = UnionFind(n)
    mst = []

    # Aplica o algoritmo de Kruskal para encontrar a MST
    for peso, u, v in arestas:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, peso))

    return mst