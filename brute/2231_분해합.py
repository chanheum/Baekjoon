import sys
n = int(sys.stdin.readline())

def solve():
    for i in range(1, n):
        # 연산의 초기값 지정
        cnt = i
        test = i
        while True:
            # 1의 자리 숫자부터 차례대로 더해주기
            cnt += (test % 10)
            test = test // 10

            # 연산을 다해줬으면 빠져나옴
            if test == 0:
                break

        # 만약 연산한 값이 원하는 값과 같으면 최소 생성자 값 출력
        if cnt == n:
            print(i)
            return
    # 연산을 끝까지해도 생성자값이 없으면 '0' 출력
    print(0)
solve()