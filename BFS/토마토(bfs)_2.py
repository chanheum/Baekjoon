from collections import deque
m, n = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = list()
max_data = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

# for i in range(len(graph)):
#     print(graph[i])
queue = deque()
def bfs(m,n,graph):
    for i in range(m):      # 0-5
        for j in range(n):  # 0-3
            if graph[j][i] == 1:
                queue.append((j,i))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == -1:
                    continue
                if graph[nx][ny] == 0:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1

bfs(m,n,graph)
for i in range(len(graph)):
    if 0 in graph[i]:
        print(-1)
        break
    else:
           max_data.append(max(graph[i]))
           #  마지막까지 연산 다했으면 출력
           if i == len(graph)-1:
            print(max(max_data) - 1)
