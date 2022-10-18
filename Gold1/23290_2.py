import sys

sys.stdin = open('BJ/test.txt', 'r')

# 23290 마법사 상어와 복제

# 0 좌 좌상 상 우상 우 우하 하 좌하
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 상 좌 하 우
ddr = [-1, 0, 1, 0]
ddc = [0, -1, 0, 1]

M, S = map(int, input().split())
grounds = [[list() for _ in range(5)] for _ in range(5)]
blood = [[0] * 5 for _ in range(5)]
for _ in range(M):
    fx, fy, d = map(int, input().split())
    grounds[fx][fy].append(d)

sx, sy = map(int, input().split())
shark_r = sx
shark_c = sy

for gr in grounds:
    print(gr)

print(shark_r, shark_c)


for idx in range(1, S + 1):
    # 1. 상어가 모든 물고기에게 복제 마법을 시전한다.
    copy_grounds = list()
    for gr in grounds:
        temp_list = list()
        for g in gr:
            temp_list.append(g[:])
        copy_grounds.append(temp_list[:])

    # 2. 모든 물고기가 한 칸 이동한다.
    # 상어 칸, 물고기 냄새 칸, 격자 범위 벗어나면 이동 불가.
    # 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향 45도 반시계 회전
    # 이동할 수 있는 칸이 없으면 그 자리로
    temp_grounds = [[list() for _ in range(5)] for _ in range(5)]

    for r in range(1, 5):
        for c in range(1, 5):
            for fish_dir in grounds[r][c]:

                for index in range(8):
                    cur_dir = (fish_dir - index) % 8
                    if cur_dir == 0:
                        cur_dir = 8
                    cr = r + dr[cur_dir]
                    cc = c + dc[cur_dir]
                    # print(cr, cc, cur_dir, '이전')
                    # 범위 안, 피 조건, 상어 없을 때
                    if 1 <= cr < 5 and 1 <= cc < 5 and blood[cr][cc] == 0 and (cr != shark_r or cc != shark_c):
                        # print(cr, cc, cur_dir, '들어옴')
                        temp_grounds[cr][cc].append(cur_dir)
                        break
                # 이동할 수 있는 칸이 없으면 그 자리로
                else:
                    temp_grounds[r][c].append(fish_dir)
    # print('after move 2')
    # for gr in temp_grounds:
    #     print(gr)

    # grounds 재설정
    grounds = list()
    for temp in temp_grounds:
        temp_list = list()
        for gr in temp:
            temp_list.append(gr[:])
        grounds.append(temp_list[:])

    # 3. 상어가 연속해서 세 칸 이동한다.
    shark_list = list()
    for move_1 in range(4):
        shark_r_1 = shark_r + ddr[move_1]
        shark_c_1 = shark_c + ddc[move_1]

        if 1 <= shark_r_1 < 5 and 1 <= shark_c_1 < 5:
            shark_eat_1 = len(grounds[shark_r_1][shark_c_1])
            for move_2 in range(4):
                shark_r_2 = shark_r_1 + ddr[move_2]
                shark_c_2 = shark_c_1 + ddc[move_2]
                if 1 <= shark_r_2 < 5 and 1 <= shark_c_2 < 5:
                    shark_eat_2 = len(grounds[shark_r_2][shark_c_2])
                    for move_3 in range(4):
                        shark_r_3 = shark_r_2 + ddr[move_3]
                        shark_c_3 = shark_c_2 + ddc[move_3]
                        if 1 <= shark_r_3 < 5 and 1 <= shark_c_3 < 5:
                            # move_1과 겹치는 곳 예방
                            if shark_r_1 != shark_r_3 or shark_c_1 != shark_c_3:
                                shark_eat_3 = len(grounds[shark_r_3][shark_c_3])
                            else:
                                shark_eat_3 = 0
                            eat = shark_eat_1 + shark_eat_2 + shark_eat_3
                            shark_list.append([eat, move_1, move_2, move_3])

    # 상어가 이동한 result_move 구하기
    result_move = [9, 9, 9]
    maximum_fish = 0
    for shark_eat, move_1, move_2, move_3 in shark_list:
        # print(shark_eat, move_1, move_2, move_3, result_move)
        if maximum_fish < shark_eat:
            maximum_fish = shark_eat
            result_move[0] = move_1
            result_move[1] = move_2
            result_move[2] = move_3
        elif maximum_fish == shark_eat:
            if result_move[0] > move_1:
                result_move[0] = move_1
                result_move[1] = move_2
                result_move[2] = move_3
            elif result_move[0] == move_1 and result_move[1] > move_2:
                result_move[0] = move_1
                result_move[1] = move_2
                result_move[2] = move_3
            elif result_move[0] == move_1 and result_move[1] == move_2 and result_move[2] > move_3:
                result_move[0] = move_1
                result_move[1] = move_2
                result_move[2] = move_3

    for move_dir in result_move:
        shark_r += ddr[move_dir]
        shark_c += ddc[move_dir]
        # 물고기가 있다면
        if grounds[shark_r][shark_c]:
            # 피 추가
            blood[shark_r][shark_c] = idx
            # 물고기 제외
            grounds[shark_r][shark_c] = list()
    # print(f"result_move: {result_move}")
    # print(f"shark_r: {shark_r}, shark_c: {shark_c}")
    # print('after shark move')
    # for gr in grounds:
    #     print(gr)

    # 4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
    for r in range(1, 5):
        for c in range(1, 5):
            if blood[r][c] + 2 <= idx:
                blood[r][c] = 0

    # print('before copy')
    # for gr in grounds:
    #     print(gr)
    # print('before copy - temp')
    # for gr in copy_grounds:
    #     print(gr)
    # 5. 1에서 사용된 복제 마법이 완료된다.
    for r in range(1, 5):
        for c in range(1, 5):
            grounds[r][c] += copy_grounds[r][c]
    #
    # print('after copy')
    # for gr in grounds:
    #     print(gr)
    # print('blood')
    # for bl in blood:
    #     print(bl)

result = 0
for r in range(1, 5):
    for c in range(1, 5):
        result += len(grounds[r][c])

print(result)

"""
grounds에서 list 다 들고다니는 것보다,
[0] * 9 하면 훨씬 더 빠르게 계산 가능.
"""