d = [0] * (40 + 1)
d[0] = 1
d[1] = 1
count_0 = 0
count_1 = 0
# 피보나치 계산 함수 (Top-Down 방식)
def fibonacci(n):
    global count_0, count_1
    if n == 0:
        count_0 += 1
        return 1
    elif n == 1:
        count_1 += 1
        return 1
    elif d[n] != 0:     # 메모이제이션 수행
        return d[n]
    else:
        d[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return d[n]

for i in range(int(input())):
    count_0, count_1 = 0, 0
    d = [0] * (40 + 1)
    d[0] = 1
    d[1] = 1
    n = int(input())
    fibonacci(n)
    # 2 이상이면 바로 뒤에 있는 피보나치 두 수를 출력한다
    if n >= 2:
        print(d[n-2], d[n-1])
    else:
        print(count_0, count_1)