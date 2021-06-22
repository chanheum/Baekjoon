dp = [5001] * 5001
array = [3,5]
n = int(input())

for j in range(3, n + 1):
    dp[3] = 1
    dp[5] = 1
    for i in range(len(array)):
        if dp[j] == 5001:
            if j % array[i] == 0:
                dp[j] = dp[j - array[i]] + 1

        dp[j] = min(dp[j], dp[j-array[i]]+1)

if dp[n] == 5001:
    print(-1)
else:
    print(dp[n])