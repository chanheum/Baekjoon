import sys
sys.setrecursionlimit(3000)

#  동북서남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    visited[x][y] = 1

    # 동북서남 서치
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if visited[nx][ny] == 1 or mapping[nx][ny] == 0:
            continue

        dfs(nx,ny)

test_case = int(input())
for T in range(test_case):
    # m : 가로
    # n : 세로
    # k : 배추가 심어진 위치 (좌표)
    m, n, k = map(int, input().split())
    # k회 배추가 심어진 위치를 입력
    mapping = [[0] * m for i in range(n)]
    visited = [[0] * m for i in range(n)]
    result = 0

    for i in range(k):
        x, y = map(int, input().split())
        mapping[y][x] = 1

    for i in range(n):      # 0 - 9
        for j in range(m):  # 0 - 7
            if mapping[i][j] == 1 and visited[i][j] == 0:
                dfs(i,j)
                result += 1

    print(result)
