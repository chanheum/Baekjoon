import sys
# 재귀 횟수 증량
sys.setrecursionlimit(2000)

# [동 북 서 남] 순서 탐색
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 입력
block = int(input())
mapping = []
count = 0
result_2 = 0
result = []
for i in range(block):
    mapping.append(list(map(int, input())))

visited = [[0] * block for i in range(block)]

# 깊이 우선 탐색
def dfs(x, y):
    # 범위 벗어나면 함수 종료
    global count
    if x < 0 or x >= block or y < 0 or y >= block:
        return
    # 노드 방문
    visited[x][y] = 1
    count += 1

    # 동북서남 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < block and ny < block and mapping[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx,ny)


for i in range(block):
    for j in range(block):
        if mapping[i][j] == 1 and visited[i][j] == 0:
            count = 0
            dfs(i,j)
            result_2 += 1
            result.append(count)

print(result_2)
result.sort()
for i in range(len(result)):
    print(result[i])