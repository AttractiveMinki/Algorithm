import sys

sys.stdin = open('BJ/test.txt', 'r')

# 20056 마법사 상어와 파이어볼

# 상 우상 우 우하 하 좌하 좌 좌상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
grounds = [[list() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    ri, ci, mi, si, di = map(int, input().split())
    grounds[ri - 1][ci - 1].append([mi, si, di])

for _ in range(K):
    # 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸만큼 이동한다.
    temp_grounds = [[list() for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for mi, si, di in grounds[r][c]:
                # (현재 위치 + 이동방향 * 거리) % N
                cr = (r + dr[di] * (si % N)) % N
                cc = (c + dc[di] * (si % N)) % N
                temp_grounds[cr][cc].append([mi, si, di])

    # 이동이 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에선 다음과 같은 일이 일어난다.
    grounds = [[list() for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if len(temp_grounds[r][c]) == 1:
                grounds[r][c] = temp_grounds[r][c][:]
            elif len(temp_grounds[r][c]) >= 2:
                # 1. 같은 칸에 있는 파이어볼은 모두 하나로 합친다.
                # 2. 파이어볼은 4개의 파이어볼로 나눠진다.
                # 3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
                total_m = 0
                total_s = 0
                total_odd = 0
                total_even = 0
                for mi, si, di in temp_grounds[r][c]:
                    total_m += mi
                    total_s += si
                    if di % 2 == 0:
                        total_even += 1
                    else:
                        total_odd += 1
                # 3-1. 질량은 (질량합 / 5) 이다.
                total_m //= 5
                # 3-2. 속력은 (속력합 / 파이어볼 갯수)이다.
                total_s //= len(temp_grounds[r][c])
                # 3-4. 질량이 0인 파이어볼은 모두 소멸된다.
                if total_m == 0:
                    continue
                # 3-3. 방향 모두 홀수거나 짝수 -> 방향 0, 2, 4, 6
                if total_odd == 0 or total_even == 0:
                    grounds[r][c].append([total_m, total_s, 0])
                    grounds[r][c].append([total_m, total_s, 2])
                    grounds[r][c].append([total_m, total_s, 4])
                    grounds[r][c].append([total_m, total_s, 6])
                else:
                    grounds[r][c].append([total_m, total_s, 1])
                    grounds[r][c].append([total_m, total_s, 3])
                    grounds[r][c].append([total_m, total_s, 5])
                    grounds[r][c].append([total_m, total_s, 7])

result = 0
for r in range(N):
    for c in range(N):
        for mi, si, di in grounds[r][c]:
            result += mi

print(result)
