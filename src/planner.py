graph = {'start': {'align': 2, 'wait': 5}, 'align': {'burn': 3}, 'burn': {'orbit': 4}, 'wait': {'orbit': 10}, 'orbit': {}}

def run():
    dist = {n:999 for n in graph}
    dist['start'] = 0
    for _ in graph:
        for u in graph:
            for v,w in graph[u].items():
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    print(dist)
