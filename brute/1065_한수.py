import sys
n = int(sys.stdin.readline().replace('\n',''))
result = 0

def brute(number):
    first = (number // 100)
    second = ((number % 100) // 10)
    third = number % 10

    # 두 자리수는 모든 수가 등차수열로 판단할 수 있음.
    if number <= 99:
        return 1
    if first - second == second - third:
        return 1
    return 0

for i in range(1, n + 1):
    if brute(i) == 1:
        result += 1
print(result)
