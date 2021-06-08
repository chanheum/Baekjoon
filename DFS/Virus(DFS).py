# 컴퓨터의 수
n = int(input()) # 1 ~ n개
# 연결되어 있는 쌍
m = int(input())
# 연결 그래프 처리
conn = [[] * n for i in range(n + 1)]
# 노드 방문 처리
visited = [0 for i in range(n + 1)]
result = 0
for i in range(m):
    num, num2 = map(int, input().split())
    conn[num].append(num2)
    conn[num2].append(num)

# print(conn)

def dfs(start):
    global result
    # 노드 방문 처리
    visited[start] = 1

    # 노드에 연결된 노드들 처리
    for node in conn[start]:
        if visited[node] == 0:
            dfs(node)
            result += 1
dfs(1)
print(result)