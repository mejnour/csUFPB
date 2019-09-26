# DIJKSTRA(G, w, s)
#     INITIALIZE-SINGLE-SOURCE(G, s)
#     S = 0
#     Q = V[G]
#     while Q != 0
#         do u = EXTRACT-MIN(Q)
#             S = S U {u}
#             for each vertex v in Adj[u]
#                 RELAX(u, v, w)

class dijkstra:
    def __init__(self, G, w, s):
        pass
    
    def initializeSingleSource(self, G, s):
        for v in V[G]:
            d[v] = infinito
            pi[v] = None
        
        d[s] = 0
    
    def extractMin(self, u, v, w):
        pass

    def extract(self, u, v, w):
        pass
    
    def relax(self, u, v, w):
        if d[v] > d[u] + w(u, v):
            d[v] = d[u] + w(u, v)
            pi[v] = u


if __name__ == "__main__":
    S = 0
    Q = V[G]
    while Q != 0:
        for u in extractMin(Q):
            S = S U u
            for v in Adj[u]:
                relax(u, v, w)