from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int,sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# print(visited)
# for i in range(n):
#     print(graph[i])

def bfs(start):
    visited[start] = 1
    q = deque([start])

    while q:
        v = q.popleft()
        for nodes in graph[v]:
            if not visited[nodes]:
                visited[nodes] = True
                q.append(nodes)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        bfs(i)

print(count)
