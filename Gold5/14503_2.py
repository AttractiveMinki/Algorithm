import sys

sys.stdin = open('test.txt', 'r')

# 14503 로봇 청소기

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
cr, cc, cd = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]

while True:
    # 1. 현재 위치 청소
    # print(f"cr: {cr}, cc: {cc} --")
    grounds[cr][cc] = 2
    
    # 4방향
    for _ in range(4):
        # 2-1. 왼쪽 아직 청소 안했으면 그 방향으로 회전 후 전진, 1번 진행
        cd = (cd - 1) % 4
        tr = cr + dr[cd]
        tc = cc + dc[cd]
        # print(f"tr: {tr}, tc: {tc}, grounds: {grounds[tr][tc]}")
        if 0 <= tr < N and 0 <= tc < M and grounds[tr][tc] == 0:
            cr = tr
            cc = tc
            break
        # 2-2. 왼쪽 방향에 청소할 공간이 없다면 그 방향으로 회전하고 2번으로 돌아감
        else:
            continue
    # 2-3. 네 방향 모두 청소가 되어 있거나 벽인 경우, 한 칸 후진 후 2번
    else:
        back_d = (cd - 2) % 4
        cr += dr[back_d]
        cc += dc[back_d]
        # 2-4. 뒤쪽이 벽이라 후진 불가시 종료
        if cr < 0 or cr >= N or cc < 0 or cc >= M or grounds[cr][cc] == 1:
            break

cnt = 0
for r in range(N):
    for c in range(M):
        if grounds[r][c] == 2:
            cnt += 1
print(cnt)

# for gr in grounds:
#     print(gr)
