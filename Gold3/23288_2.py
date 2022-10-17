import sys

sys.stdin = open('BJ/test.txt', 'r')

# 23288 주사위 굴리기 2

def move_dice(cur_dir):
    # 위로 이동
    if cur_dir == 0:
        temp_num = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = temp_num

    # 왼쪽으로 이동
    elif cur_dir == 1:
        temp_num = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = dice[1][0]
        dice[1][0] = temp_num

    # 아래쪽으로 이동
    elif cur_dir == 2:
        temp_num = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = temp_num

    # 오른쪽으로 이동
    elif cur_dir == 3:
        temp_num = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = dice[1][2]
        dice[1][2] = temp_num

    return

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, M, K = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]
dice = [
    [0, 2, 0],
    [4, 1, 3],
    [0, 5, 0],
    [0, 6, 0]
]

cur_r = 0
cur_c = 0
cur_dir = 3
total_score = 0

for _ in range(K):
    # 1. 주사위가 이동 방향으로 한 칸 굴러간다.
    tr = cur_r + dr[cur_dir]
    tc = cur_c + dc[cur_dir]
    if 0 <= tr < N and 0 <= tc < M:
        pass
    # 1-1. 만약 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    else:
        cur_dir = (cur_dir + 2) % 4
        tr = cur_r + dr[cur_dir]
        tc = cur_c + dc[cur_dir]

    cur_r = tr
    cur_c = tc
    # 주사위도 이동시킨다.
    move_dice(cur_dir)
    # 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    temp_score = 0
    visited = [[0] * M for _ in range(N)]
    visited[cur_r][cur_c] = 1
    my_num = grounds[cur_r][cur_c]
    queue = [[cur_r, cur_c]]
    cnt = 1
    while queue:
        qr, qc = queue.pop(0)
        for i in range(4):
            cr = qr + dr[i]
            cc = qc + dc[i]
            if 0 <= cr < N and 0 <= cc < M and visited[cr][cc] == 0 and grounds[cr][cc] == my_num:
                visited[cr][cc] = 1
                queue.append([cr, cc])
                cnt += 1

    total_score += (my_num * cnt)

    # 3. 주사위의 아랫면에 있는 정수 A와 x, y에 있는 B를 비교해 이동 방향을 결정한다.
    A = dice[3][1]
    B = grounds[cur_r][cur_c]
    # 3-1. A > B인 경우 이동 방향 90도 시계 방향 회전
    if A > B:
        cur_dir = (cur_dir - 1) % 4
    # 3-2. A < B인 경우 90도 반시계방향
    elif A < B:
        cur_dir = (cur_dir + 1) % 4
    # 3-3. A == B인 경우 변화 X


print(total_score)
