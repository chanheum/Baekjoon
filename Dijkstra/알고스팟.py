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
# 다익스트라 알고리즘 수행
def dijkstra(x,y):
    q = []
    heapq.heappush(q, (x,y))
    # 초기 시작점에 대한 거리 초기화
    distance[x][y] = 0

    while q:
        rx, ry = heapq.heappop(q)
        for i in range(4):
            nx = rx + dx[i]
            ny = ry + dy[i]
            # 범위를 벗어나면, 무시.
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            # 방문한 노드가 '벽'이면
            if graph[nx][ny] == 1:
                # 기존 횟수에 +1한 값을 넣어줌.
                if distance[nx][ny] > distance[rx][ry] + 1:
                    distance[nx][ny] = distance[rx][ry] + 1
                    heapq.heappush(q, (nx,ny))
            elif graph[nx][ny] == 0:
                if distance[nx][ny] > distance[rx][ry]:
                    distance[nx][ny] = distance[rx][ry]
                    heapq.heappush(q, (nx, ny))

dijkstra(0,0)
print(distance[m - 1][n - 1])