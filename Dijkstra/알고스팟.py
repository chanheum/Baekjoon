import sys
import heapq
INF = int(1e9)
graph = []
n,m = map(int,sys.stdin.readline().split())
distance = [[INF] * (n) for _ in range(m)]

for i in range(m):
    graph.append(list(map(int,sys.stdin.readline().replace('\n',''))))

# 동서남북
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dijkstra(x,y):
    q = []
    heapq.heappush(q, (x,y))
    distance[x][y] = 0

    while q:
        rx, ry = heapq.heappop(q)
        for i in range(4):
            nx = rx + dx[i]
            ny = ry + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[nx][ny] == 1:
                if distance[nx][ny] > distance[rx][ry] + 1:
                    distance[nx][ny] = distance[rx][ry] + 1
                    heapq.heappush(q, (nx,ny))
            elif graph[nx][ny] ==0:
                if distance[nx][ny] > distance[rx][ry]:
                    distance[nx][ny] = distance[rx][ry]
                    heapq.heappush(q, (nx, ny))

dijkstra(0,0)
print(distance[m - 1][n - 1])
