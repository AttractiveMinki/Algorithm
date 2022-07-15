# 1932 정수 삼각형 - 주석

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

# N 길이의 dp 선언
dp = [0] * N
dp[0] = numbers[0][0]

# 삼격형 레벨, 층 세는 level. 일종의 행
for level in range(1, N):
    # 층 안에서 위치 알려주는 i, 일종의 열
    # 앞에서부터 계산하면, dp의 뒤의 연산에 영향을 미치므로
    # 뒤에서부터 계산한다.
    for i in range(level, -1, -1):
        # 마지막 열 예외처리
        if i == level + 1:
            dp[i] = dp[i - 1] + numbers[level][i]
        # 첫 열 예외처리
        elif i == 0:
            dp[i] = dp[0] + numbers[level][i]
        # 마지막이나 첫 열이 아닐 경우, dp[i], dp[i - 1] 중 큰 값을 가져와 연산한다.
        else:
            dp[i] = max(dp[i], dp[i - 1]) + numbers[level][i]

print(max(dp))

"""
3
1
1 2
1 2 3

dp = [0, 0, 0]
첫 level 입력(dp[0] = numbers[0][0])
dp = [1, 0, 0]


두 번째 level = 1, i = 1
# 마지막 열 예외처리
dp[1] = dp[0] + numbers[1][1] = 1 + 2 = 3
dp = [1, 3, 0]

두 번째 level = 1, i = 0
# 첫 열 예외처리
dp[0] = dp[0] + numbers[1][0] = 1 + 1 = 2
dp = [2, 3, 0]

## i를 거꾸로 연산하지 않고 i=0, 1, 2, ... 순으로 본다면,
## i=0에서의 dp 연산이 i=1에서의 dp 연산에 영향을 미치기 때문에, i에 거꾸로 접근하였다.

세 번째 level = 2, i = 2
# 마지막 열 예외처리
dp[2] = dp[1] + numbers[2][2] = 3 + 3 = 6
dp = [2, 3, 6]

세 번째 level = 2, i = 1
dp[1] = max(dp[1], dp[0]) + numbers[2][1] = 3 + 2 = 5
dp = [2, 5, 6]

세 번째 level = 2, i = 0
# 첫 열 예외처리
dp[0] = dp[0] + numbers[2][0] = 2 + 1 = 3
dp = [3, 5, 6]

"""
