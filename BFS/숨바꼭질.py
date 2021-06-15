from collections import deque
n, m = map(int,input().split())
MAX = 10**5
# 노드 방문 처리
visited = [False] * (MAX+1)
# 노드 방문 차례를 나타낼 변수
graph = [0] * (MAX+1)

def bfs(n):
    queue = deque([n])
    visited[n] = True

    while queue:
        now = queue.popleft()
        for next in (now-1, now+1, now*2):
            if 0 <= next <= MAX and visited[next] == False:
                visited[next] = True
                queue.append(next)
                graph[next] = graph[now] + 1

    return graph[m]

print(bfs(n))
