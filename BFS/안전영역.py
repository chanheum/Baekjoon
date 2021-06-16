from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y, num):
    visited[x][y] = 1
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < m:
                if visited[nx][ny] == 0 and (graph[nx][ny] - num) > 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))

m = int(input())
# m * m 크기의 방문처리 변수 생성
visited = [[0] * (m) for _ in range(m)]
graph = []
max_num = 0
for i in range(m):
    graph.append(list(map(int,input().split(' '))))
    # 입력 받을 때부터 높이의 최대 값을 저장해둔다.
    if max(graph[i]) > max_num:
        max_num = max(graph[i])
result = [0 for _ in range(max_num)]
for num in range(0, max_num + 1):  # 0 - 9
    # 각 높이별 안전영역을 구하려할 때마다 방문 정보는 초기화 해준다.
    visited = [[0] * (m) for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if visited[i][j] == 0 and (graph[i][j] - num) > 0:
                bfs(i,j,num)
                result[num] += 1

# print(max(result))
print(result)
