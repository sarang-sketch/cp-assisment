# UVA 10305 - Ordering Tasks
# https://onlinejudge.org/external/103/10305.pdf
#
# Topological sort of a directed graph.

import sys
from collections import deque

def solve():
    while True:
        line = input().split()
        n, m = int(line[0]), int(line[1])
        if n == 0 and m == 0:
            break
        
        adj = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        
        for _ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)
            indeg[v] += 1
        
        # Kahn's algorithm (BFS topological sort)
        queue = deque()
        for i in range(1, n + 1):
            if indeg[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            u = queue.popleft()
            result.append(str(u))
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)
        
        print(' '.join(result))

if __name__ == "__main__":
    solve()
