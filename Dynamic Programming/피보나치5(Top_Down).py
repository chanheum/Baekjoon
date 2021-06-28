# 연산에 대한 정답을 백업할 dp 테이블 정의.
dp = [0] * 21
def fbn(num):
    if 0 <= num <= 1:
        return num
    if dp[num] != 0:
        return dp[num]
    # Memoization (한번 계산한 연산 결과는 메모해 둔다)
    dp[num] = fbn(num-1)+fbn(num-2)
    return dp[num]

n = int(input())
print(fbn(n))