class ConjuntoDisjunto:
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def encontrar(self, u):
        if self.pai[u] != u:
            self.pai[u] = self.encontrar(self.pai[u])
        return self.pai[u]

    def unir(self, u, v):
        raiz_u = self.encontrar(u)
        raiz_v = self.encontrar(v)
        if raiz_u != raiz_v:
            if self.rank[raiz_u] > self.rank[raiz_v]:
                self.pai[raiz_v] = raiz_u
            elif self.rank[raiz_u] < self.rank[raiz_v]:
                self.pai[raiz_u] = raiz_v
            else:
                self.pai[raiz_v] = raiz_u
                self.rank[raiz_u] += 1

def gerar_mst(matriz_adjacencia):
    n = len(matriz_adjacencia)
    arestas = []

    for i in range(n):
        for j in range(i + 1, n):
            if matriz_adjacencia[i][j] != 0:
                arestas.append((matriz_adjacencia[i][j], i, j))

    arestas.sort()
    cd = ConjuntoDisjunto(n)
    mst = []

    for peso, u, v in arestas:
        if cd.encontrar(u) != cd.encontrar(v):
            cd.unir(u, v)
            mst.append((u, v, peso))

    return mst
