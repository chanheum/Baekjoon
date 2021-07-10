import sys
import heapq
INF = int(1e9)
n, m = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    # a에서 b로가는 경로의 비용이 'c'이다.
    graph[a].append((b,c))

def dijkstra(start):
    # 빈 큐에 시작점에 대한 연결정보 넣기
    q = []
    # 거리를 우선순위로 q에 넣는다.
    heapq.heappush(q, (0, start))
    # 시작점에 대한 처리
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 이미 기록되어 있는 노드로 가는 최단경로가
        # 노드로 가는 비용보다 작으면
        # 이미 처리 된 것으로 판단
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])