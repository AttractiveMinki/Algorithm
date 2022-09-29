import sys

sys.stdin = open('BJ/test.txt', 'r')

# 20058 마법사 상어와 파이어볼

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, Q = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))

for magic_num in L:
    temp_grounds = [gr[:] for gr in grounds]
    # 회전 마법
    # 마법을 시작할 각 격자의 0행 0열을 r, c로 표현
    for r in range(0, 2 ** N, 2 ** magic_num):
        for c in range(0, 2 ** N, 2 ** magic_num):
            
            # 격자 안에서 탐색하며 시계방향으로 90도 회전
            for tr in range(r, r + 2 ** magic_num):
                for tc in range(c, c + 2 ** magic_num):
                    # r값은 tc - (c - r)
                    # c값은 (r + c + length(2 ** magic_num) - 1) - tr
                    grounds[tc - (c - r)][(r + c + 2 ** magic_num - 1) - tr] = temp_grounds[tr][tc]

    temp_grounds = [gr[:] for gr in grounds]
    # 3칸 이상 얼음 인접하지 않을 경우 -= 1
    for r in range(2 ** N):
        for c in range(2 ** N):
            cnt = 0
            for i in range(4):
                cr = r + dr[i]
                cc = c + dc[i]
                if 0 <= cr < 2 ** N and 0 <= cc < 2 ** N and temp_grounds[cr][cc] > 0:
                    cnt += 1
            if cnt < 3 and temp_grounds[r][c] > 0:
                grounds[r][c] -= 1

result1 = 0
result2 = 0
visited = [[0] * 2 ** N for _ in range(2 ** N)]
for r in range(2 ** N):
    # resul1 계산
    result1 += sum(grounds[r])

    # result2 계산
    for c in range(2 ** N):
        temp_result2 = 0
        if visited[r][c] == 0 and grounds[r][c] > 0:
            temp_result2 += 1
            visited[r][c] = 1
            queue = [[r, c]]
            while queue:
                qr, qc = queue.pop(0)
                for i in range(4):
                    tr = qr + dr[i]
                    tc = qc + dc[i]
                    if 0 <= tr < 2 ** N and 0 <= tc < 2 ** N and visited[tr][tc] == 0 and grounds[tr][tc] > 0:
                        temp_result2 += 1
                        visited[tr][tc] = 1
                        queue.append([tr, tc])
            result2 = max(temp_result2, result2)
# print('result')
# print(f"L: {magic_num} result1: {result1}, result2: {result2}")
# for gr in grounds:
#     print(gr)

print(result1)
print(result2)

"""
예제 4에서 원하는 결과가 나오지 않았다.
result2을 60으로 계산했는데, 답은 62였다.
코드 뜯어본 결과, 3칸 이상 얼음에 인접하지 않은 경우 -1을 해주는 과정에서
grounds를 참조하고 있었기 때문에, grounds[r][c] = 1이라면
grounds[r][c] -= 1 -> grounds[r][c] = 0이 되고,
이는 grounds[r + 1][c]나 grounds[r][c + 1]을 계산할 때 영향을 주었다.
temp_grounds에 grounds 값을 복사하고, temp_grounds를 기반으로 계산하여 문제를 해결하였다.

0, 0 ~ 3, 3과 같이 정해진 형태의 정사각형 모양에서, 시계/반시계 방향으로 90도 회전하는 것은 쉬웠지만
문제처럼 모든 격자에 대해서 회전시키는 것은 쉽지 않았다.
공책에 그려가며 일반식을 찾았고, 일반식은 다음과 같다.
격자 내에서 첫 행 첫 열을 r, c라 하고,
현재 보고 있는 행, 열을 tr, tc라고 하면
r -> tc - (c - r)
c -> r + c + length - 1 - tr
여기서 length는 격자 내에서 행이나 열의 길이를 뜻한다.
코드에선 2 ** magin_num으로 length를 구하였다.


후기
문제가 한 눈에 들어오지 않아 여러 번 읽었다.
실제 문제를 풀 때엔 친절한 예시가 주어지는데,
백준에선 예시가 주어지지 않아 문제를 세 번 정독하는 과정에서 문제를 이해할 수 있었다.
문제를 이해하고 나서, 격자를 어떻게 나눌지 먼저 걱정하였고
각 격자 내에서 회전을 어떻게 시키나 막막하였다.
구체적으로 어떻게 풀지 감이 오지 않는 상황에서, 먼저 격자를 나눠보자고 생각했다.
L=1일 때 2*2, L=2일 때 4*4, L=3일 때 8*8 격자로 나눠지므로
2 ** L 꼴로 나누면 되겠다고 생각했다.
이를 위해 격자를 그리기 시작하는 행과 열의 위치를 찾고, 그 안에서 r, c값을 바탕으로 90도 회전시키는 계획을 세웠다.
일반식을 찾아내었고, 그 이후엔 상대적으로 간단하게 문제를 해결할 수 있었다.
L=0일 때 식이 성립하는지 고려하지 않고 짰는데, 2**0=1이라서 90도 회전시키지 않아도 되었다.

result1, result2를 구하는 식을 for magic_num in L: 안에 넣어서,
한 사이클이 끝날 때마다 어떻게 결과가 출력되는지 눈으로 확인하며 디버깅한 덕분에,
잘못된 부분을 빠르게 찾아낼 수 있었다.

한 시간정도 소요된 것 같다. 실전에서도 지금처럼만 풀 수 있길 바란다.
"""
