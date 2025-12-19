from .graph import graph
def solve(start):
    dist = {n:999 for n in graph}
    dist[start]=0
    for _ in graph:
        for u in graph:
            for v,w in graph[u].items():
                if dist[u]+w < dist[v]:
                    dist[v]=dist[u]+w
    return dist

def run():
    print(solve("start"))
