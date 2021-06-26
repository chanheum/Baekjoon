t = int(input())

def go(count, sum, goal):
    if count > 11:
        return 0
    if sum > goal:
        return 0
    if sum == goal:
        return 1
    now = 0
    for i in range(1,3+1):
        now += go(count+1, sum + i, goal)
    return now


while t:
    t -= 1
    print(go(0,0,int(input())))