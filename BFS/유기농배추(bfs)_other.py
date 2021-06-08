from collections import deque
# 테스트 케이스 입력받기
t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# bfs함수 구현하기
def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표 범위 내에 있다면
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if field[nx][ny] == 1:
                    # 동서남북으로 배추가 심어져 있는 곳은 Queue에 넣기
                    queue.append((nx,ny))
                    # 배추 심은 곳을 2로 바꾸어 놓기
                    field[nx][ny] = 2

for i in range(t):
    # 가로,세로,배추의 개수 입력받기
    m,n,k = map(int, input().split())

    # 재배하는 땅 리스트로 초기화하기
    field = [[0] * m for _ in range(n)]

    # 배추 정보 입력 받기
    for i in range(k):
        a,b = map(int, input().split())
        field[b][a] = 1

    # 지렁이 개수를 셀 변수 초기화하기
    count = 0

    # 지렁이 개수 세기
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i,j)
                count += 1

    print(count)