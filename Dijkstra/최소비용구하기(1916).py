import sys
import heapq
# 초기 데이터 삽입을 위한 무한대 값 설정
INF = int(1e9)
# 도시의 개수
n = int(sys.stdin.readline())
# 버스의 개수
m = int(sys.stdin.readline())
# 도시 연결 및 비용에 대한 정보를 담는 변수
graph = [[] for _ in range(n + 1)]
# 최소비용을 저장하는 변수
distance = [INF] * (n + 1)
for _ in range(m):
    a,b,cost = map(int, sys.stdin.readline().split())
    # a에서 b로 가는데 드는 비용이 cost
    graph[a].append((b,cost))
start, end = map(int, sys.stdin.readline().split())

def dijkstra(start):
    q = []
    # 시작 노드에 대한 시작 비용 '0'
    distance[start] = 0
    # 최소비용 우선순위 q
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        # 이미 도착했었던 노드라면 무시.
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            # 기존 비용 테이블보다 더 작은 비용이 발생하면 테이블 최소비용 반영
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                # 최소비용 우선순위 q
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end])