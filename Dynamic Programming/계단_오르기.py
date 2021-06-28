# 300이하의 자연수
dp = [0] * 301

n = int(input())
array = [0]
for _ in range(n):
    array.append((int(input())))
    
# 계단이 1개인 경우에 대비해서 2 이상일 때만 테이블 '2'까지 초기값 지정
if n >= 2:
    dp[2] = array[1] + array[2]

dp[0] = array[0]
dp[1] = array[1]
# 다이나믹 프로그래밍 실행
# 마지막 계단을 기준으로 1칸 띄었을 때 or 2칸 띄었을 때에 대한 비교 연산
for i in range(3, n + 1):
    dp[i] = max(dp[i-2] + array[i], dp[i-3] + array[i] + array[i-1])
print(dp[n])