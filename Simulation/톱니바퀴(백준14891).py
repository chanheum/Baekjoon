import sys
from collections import deque
gears = {}
for i in range(1, 4+1):
    gears[i] = deque(list(map(int,list(sys.stdin.readline().replace('\n','')))))

def check_right(start, dirs):
    if start > 4 or gears[start-1][2] == gears[start][6]:
        return

    if gears[start-1][2] != gears[start][6]:
        check_right(start + 1, -dirs)
        gears[start].rotate(dirs)

def check_left(start, dirs):
    if start < 1 or gears[start][2] == gears[start+1][6]:
        return

    if gears[start + 1][6] != gears[start][2]:
        check_left(start - 1, -dirs)
        gears[start].rotate(dirs)

k = int(input())

for _ in range(k):
    num , dirs = map(int, input().split())

    check_right(num + 1, -dirs)
    check_left(num - 1, -dirs)
    gears[num].rotate(dirs)

result = 0
for i in range(4):
    result += (2**i) * gears[i+1][0]

print(result)