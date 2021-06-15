from collections import deque
# 동서남북 + 대각선
search_direction_x = [1,-1,0,0,-1,1,-1,1]
search_direction_y = [0,0,1,-1,1,-1,-1,1]

def bfs(x,y):
    visited[x][y] = 1
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 8개 방향에 대한 탐색
        for i in range(8):
            nx = x + search_direction_x[i]
            ny = y + search_direction_y[i]

            # 만약 그래프 탐색하다가 index out of range 발생하면 for문 안에 있는 x,y 축의 기준 변수만 바꿔준다. (nx를 h와 비교, ny를 w와 비교)
            # 탐색한 곳이 범위 안에 들어가 있으면
            if nx >= 0 and ny >= 0 and nx < h and ny < w:
                if visited[nx][ny] == 0 and map_info[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))

while True:
    w, h = map(int,input().split(' '))
    map_info = []
    visited = [[0] * (w) for _ in range(h)]
    result = 0
    # 맵의 크기가 '0'이면 프로그램을 끝낸다
    if w == 0 and h == 0:
        break

    for _ in range(h):
        map_info.append(list(map(int,input().split())))
    # 만약 그래프 탐색하다가 index out of range 발생하면 for문 안에 있는 x,y 축의 기준 변수만 바꿔준다. (여기서는 w,h만 바꿔주면 되지)
    for j in range(w):      # 0 - 4
        for i in range(h):  # 0 - 3
            if visited[i][j] == 0 and map_info[i][j] == 1:
                result += 1
                bfs(i,j)

    print(result)
