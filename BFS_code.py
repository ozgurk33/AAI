from collections import deque

def bfs(adj):
    V = len(adj)
    visited = [False] * V
    res = []

    src = 0
    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    return res

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    V = 5
    adj = []

    for i in range(V):
        adj.append([])

    addEdge(adj, 1, 2)
    addEdge(adj, 1, 0)
    addEdge(adj, 2, 0)
    addEdge(adj, 2, 3)
    addEdge(adj, 2, 4)

    res = bfs(adj)

    for node in res:
        print(node, end=" ")
