import sys

sys.stdin = open('BJ/test.txt', 'r')

# 23289 온풍기 안녕!

def wind(heat_r, heat_c, heat_dir):
    # print(f"heat_r: {heat_r}, heat_c: {heat_c}, heat_dir: {heat_dir}")
    temp_heat = [[0] * C for _ in range(R)]
    heat_r += dr[heat_dir]
    heat_c += dc[heat_dir]
    # 범위 안에 있다면
    if 0 <= heat_r < R and 0 <= heat_c < C:
        temp_heat[heat_r][heat_c] = 5
        queue = [[heat_r, heat_c, heat_dir, 4]]
    else:
        return temp_heat

    while queue:
        qr, qc, qdir, qdis = queue.pop(0)
        ## 직진 ##
        sr = qr + dr[qdir]
        sc = qc + dc[qdir]
        if 0 <= sr < R and 0 <= sc < C:
            # 벽이 있다면 continue
            skip = 0
            if walls[qr][qc] and qdir in walls[qr][qc]:
                skip = 1
            elif walls[sr][sc] and (qdir - 2) % 4 in walls[sr][sc]:
                skip = 1
            # for wall_r, wall_c, wall_dir in walls:
            #     if qr == wall_r and qc == wall_c and qdir == wall_dir:
            #         skip = 1
            #         break
            #     elif sr == wall_r and sc == wall_c and (qdir - 2) % 4 == wall_dir:
            #         skip = 1
            #         break
            if skip != 1:
                temp_heat[sr][sc] = qdis
                if qdis - 1 > 0:
                    queue.append([sr, sc, qdir, qdis - 1])

        ## 위로 갔다가 직진 ##
        # 위로
        upper_dir = (qdir + 1) % 4
        ur = qr + dr[upper_dir]
        uc = qc + dc[upper_dir]
        if 0 <= ur < R and 0 <= uc < C:
            # 벽이 있다면 continue
            skip = 0
            if walls[qr][qc] and upper_dir in walls[qr][qc]:
                skip = 1
            elif walls[ur][uc] and (upper_dir - 2) % 4 in walls[ur][uc]:
                skip = 1
            # for wall_r, wall_c, wall_dir in walls:
            #     if qr == wall_r and qc == wall_c and upper_dir == wall_dir:
            #         skip = 1
            #         break
            #     elif ur == wall_r and uc == wall_c and (upper_dir - 2) % 4 == wall_dir:
            #         skip = 1
            #         break
            if skip != 1:
                # print('skip 안됐쥬1', qr, qc)
                # 직진
                sr = ur + dr[qdir]
                sc = uc + dc[qdir]
                if 0 <= sr < R and 0 <= sc < C:
                    # 벽이 있다면 continue
                    skip = 0
                    if walls[ur][uc] and qdir in walls[ur][uc]:
                        skip = 1
                    elif walls[sr][sc] and (qdir - 2) % 4 in walls[sr][sc]:
                        skip = 1
                    # for wall_r, wall_c, wall_dir in walls:
                    #     if ur == wall_r and uc == wall_c and qdir == wall_dir:
                    #         skip = 1
                    #         break
                    #     elif sr == wall_r and sc == wall_c and (qdir - 2) % 4 == wall_dir:
                    #         skip = 1
                    #         break
                    if skip != 1:
                        # print('skip 안됐쥬2', qr, qc)
                        temp_heat[sr][sc] = qdis
                        if qdis - 1 > 0:
                            queue.append([sr, sc, qdir, qdis - 1])
                        
        ## 아래로 갔다가 직진 ##
        # 아래로
        down_dir = (qdir - 1) % 4
        down_r = qr + dr[down_dir]
        down_c = qc + dc[down_dir]
        if 0 <= down_r < R and 0 <= down_c < C:
            # 벽이 있다면 continue
            skip = 0
            if walls[qr][qc] and down_dir in walls[qr][qc]:
                skip = 1
            elif walls[down_r][down_c] and (down_dir - 2) % 4 in walls[down_r][down_c]:
                skip = 1
            # for wall_r, wall_c, wall_dir in walls:
            #     if qr == wall_r and qc == wall_c and down_dir == wall_dir:
            #         skip = 1
            #         break
            #     elif down_r == wall_r and down_c == wall_c and (down_dir - 2) % 4 == wall_dir:
            #         skip = 1
            #         break
            if skip != 1:
                # print('skip 안됐쥬3', qr, qc)
                # 직진
                sr = down_r + dr[qdir]
                sc = down_c + dc[qdir]
                if 0 <= sr < R and 0 <= sc < C:
                    # 벽이 있다면 continue
                    skip = 0
                    if walls[down_r][down_c] and qdir in walls[down_r][down_c]:
                        skip = 1
                    elif walls[sr][sc] and (qdir - 2) % 4 in walls[sr][sc]:
                        skip = 1
                    # for wall_r, wall_c, wall_dir in walls:
                    #     if down_r == wall_r and down_c == wall_c and qdir == wall_dir:
                    #         skip = 1
                    #         break
                    #     elif sr == wall_r and sc == wall_c and (qdir - 2) % 4 == wall_dir:
                    #         skip = 1
                    #         break
                    if skip != 1:
                        # print('skip 안됐쥬4', qr, qc)
                        temp_heat[sr][sc] = qdis
                        if qdis - 1 > 0:
                            queue.append([sr, sc, qdir, qdis - 1])

    return temp_heat


# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

R, C, K = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(R)]
heater = list()
get_temp_list = list()
walls = [[list() for _ in range(C)] for _ in range(R)]
total_tempo = [[0] * C for _ in range(R)]
chocolate = 0

for r in range(R):
    for c in range(C):
        # 오른쪽
        if grounds[r][c] == 1:
            heater.append([r, c, 3])
        # 왼쪽
        elif grounds[r][c] == 2:
            heater.append([r, c, 1])
        # 위쪽
        elif grounds[r][c] == 3:
            heater.append([r, c, 0])
        # 아래쪽
        elif grounds[r][c] == 4:
            heater.append([r, c, 2])
        # 온도 조사
        elif grounds[r][c] == 5:
            get_temp_list.append([r, c])

W = int(input())
for _ in range(W):
    x, y, t = map(int, input().split())
    # walls.append([x - 1, y - 1, t])
    x -= 1
    y -= 1
    if t == 0:
        # x, y 위에 벽이 있다.
        walls[x][y].append(0)
        # walls.append([x, y, 0])
        # x - 1, y 아래에 벽이 있다.
        walls[x - 1][y].append(2)
        # walls.append([x - 1, y, 2])
    else:
        # x, y 오른쪽에 벽이 있다.
        walls[x][y].append(3)
        # walls.append([x, y, 3])
        # x, y + 1 왼쪽에 벽이 있다.
        walls[x][y + 1].append(1)
        # walls.append([x, y + 1, 1])

#
# print('walls')
# for wa in walls:
#     print(wa)

for _ in range(101):
    # 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
    temp_gr = [[0] * C for _ in range(R)]
    for heat_r, heat_c, heat_dir in heater:
        temp_heat = wind(heat_r, heat_c, heat_dir)
        for temp_r in range(R):
            for temp_c in range(C):
                temp_gr[temp_r][temp_c] += temp_heat[temp_r][temp_c]

        # print('temp')
        # for te in temp_heat:
        #     print(te)

    # print('result')
    # for te in temp_gr:
    #     print(te)

    for r in range(R):
        for c in range(C):
            total_tempo[r][c] += temp_gr[r][c]

    # 2. 온도가 조절됨
    temp_gr = [[0] * C for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            visited[r][c] = 1
            for dir in range(4):
                cr = r + dr[dir]
                cc = c + dc[dir]
                if 0 <= cr < R and 0 <= cc < C and visited[cr][cc] == 0:
                    # 벽이 있다면 continue
                    skip = 0
                    if walls[r][c] and dir in walls[r][c]:
                        skip = 1
                    elif walls[cr][cc] and (dir - 2) % 4 in walls[cr][cc]:
                        skip = 1
                    # for wall_r, wall_c, wall_dir in walls:
                    #     if r == wall_r and c == wall_c and dir == wall_dir:
                    #         skip = 1
                    #         break
                    #     elif cr == wall_r and cc == wall_c and (dir - 2) % 4 == wall_dir:
                    #         skip = 1
                    #         break
                    if skip != 1:
                        cur_tempo = total_tempo[r][c]
                        move_tempo = total_tempo[cr][cc]
                        diff = abs(cur_tempo - move_tempo) // 4
                        # 현재 온도가 더 높음
                        if cur_tempo > move_tempo:
                            temp_gr[r][c] -= diff
                            temp_gr[cr][cc] += diff
                        # 이동한 온도가 더 높음
                        elif cur_tempo < move_tempo:
                            temp_gr[r][c] += diff
                            temp_gr[cr][cc] -= diff

    # print('result')
    # for te in temp_gr:
    #     print(te)

    # 연산 결과 집어넣기
    for r in range(R):
        for c in range(C):
            total_tempo[r][c] += temp_gr[r][c]

    # print('--')
    # for to in total_tempo:
    #     print(to)

    # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    for c in range(C):
        # 맨 윗줄
        if total_tempo[0][c] > 0:
            total_tempo[0][c] -= 1
        # 맨 아랫줄
        if total_tempo[R - 1][c] > 0:
            total_tempo[R - 1][c] -= 1

    for r in range(1, R - 1):
        # 맨 왼쪽
        if total_tempo[r][0] > 0:
            total_tempo[r][0] -= 1
        # 맨 오른쪽
        if total_tempo[r][C - 1] > 0:
            total_tempo[r][C - 1] -= 1

    # print('감소')
    # for to in total_tempo:
    #     print(to)

    # 4. 초콜렛 하나 먹는다.
    chocolate += 1

    # 5. 조사하는 모든 칸 온도가 K 이상이면 중단.
    for cur_r, cur_c in get_temp_list:
        if total_tempo[cur_r][cur_c] < K:
            break
    else:
        break
# if chocolate >= 100:
#     chocolate = 101
# for to in total_tempo:
#     print(to)
#
# print('==')
print(chocolate)

"""
시간 초과
walls 리스트 하나하나 비교 -> walls라는 배열을 만들어버림
"""