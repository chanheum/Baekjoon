import sys
n = int(sys.stdin.readline())
data = []

for _ in range(n):
    data.append(tuple(map(int, sys.stdin.readline().split())))

def solve():
    for i in range(n):
        rank = 1
        for j in range(n):
            # 같은 것끼리는 비교할 수 없으므로 스킵
            if i == j:
                continue

            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                rank += 1

        print(rank)

solve()