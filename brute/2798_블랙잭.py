import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(n - 2):              # 0 - 4
    for j in range(i + 1, n - 1):   # i -
        for k in range(j + 1, n):   # j
            if num[i] + num[j] + num[k] <= m and result < num[i] + num[j] + num[k]:
                result = num[i] + num[j] + num[k]
print(result)