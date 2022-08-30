import sys

sys.stdin = open('test.txt', 'r')

# 2156 포도주 시식

N = int(input())

numbers = [int(input()) for _ in range(N)]
results = [0] * 3

for num in numbers:
    temp1 = max(results[0], results[1], results[2])
    results[2] = results[1] + num
    results[1] = results[0] + num
    results[0] = temp1

print(max(results))

"""
예제
        0   6   10  13  9   8   1
지금    0   0   6   16  23  28  33
이전    0   6   10  19  25  31  29
전전    0   6   16  23  28  33  31

지금 = 지금 안먹음
이전, 전전 중 제일 큰 값을 그대로 가져옴
이전, 전전 -> 지금 값을 먹음 -> += 지금

생각해 낸 다른 예시
6 6 500 13 900 8 100 # 정답: 1506
4 9000 1 1 9000 # 정답: 18001
5 900 1 1 1 900 # 정답: 1802
8 1 1 900 900 900 500 900 1 # 정답: 3201


결과: 4% 틀렸습니다.
원인: 두 번 연속 안 먹어도 된다.
예외: 
10
0
0
10
0
5
10
0
0
1
10

출력: 35
정답: 36

temp1 = max(results[1], results[2])
를
temp1 = max(results[0], results[1], results[2])
로 변경
"""
