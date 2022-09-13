import sys

sys.stdin = open('test.txt', 'r')

# 3190 뱀

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
grounds = [[0] * (N + 1) for _ in range(N + 1)]
visited = [[0] * (N + 1) for _ in range(N + 1)]
K = int(input())
for _ in range(K):
    tr, tc = map(int, input().split())
    grounds[tr][tc] = 1
    visited[tr][tc] = 2

turn_info = list()
L = int(input())
for _ in range(L):
    time, dir = input().split()
    turn_info.append([int(time), dir])


time = 0
queue = list()
queue.append([1, 1]) # r, c, 머리방향
visited[1][1] = 1
cur_dir = 0
while True:
    qr, qc = queue[-1][0], queue[-1][1]
    tr = qr + dr[cur_dir]
    tc = qc + dc[cur_dir]
    # 범위 안에 있고 기존 뱀과 겹치지 않는다면
    if 0 < tr <= N and 0 < tc <= N and visited[tr][tc] != 1:
        queue.append([tr, tc])
        visited[tr][tc] = 1
        # 사과가 없다면
        if grounds[tr][tc] == 0:
            # 끝의 몸 땡기기
            visited[queue[0][0]][queue[0][1]] = 0
            queue.pop(0)
        else:
            grounds[tr][tc] = 0

    # 범위 안에 없거나 기존 뱀과 겹친다면
    else:
        time += 1
        break
    time += 1

    # 회전을 해야할 때
    if turn_info and turn_info[0][0] == time:
        if turn_info[0][1] == 'D': # 우회전
            cur_dir += 1
        elif turn_info[0][1] == 'L': # 좌회전
            cur_dir -= 1
        cur_dir %= 4
        turn_info.pop(0)
    
print(time)
