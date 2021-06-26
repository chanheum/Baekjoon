# dp[n] : n을 1,2,3의 합으로 만들 수 있는 경우의 수

dp = [0] * (11+1)
t = int(input())

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

while t:
    t -= 1
    n = int(input())
    for i in range(4, n + 1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[n])