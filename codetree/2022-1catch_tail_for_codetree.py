import sys

sys.stdin = open('./test.txt', 'r')

# 꼬리잡기놀이

def move(temp_list):
    # print(f"temp_list: {temp_list}")
    # 머리 수정
    head_r = temp_list[0][0]
    head_c = temp_list[0][1]
    # print(f"head_r: {head_r}, head_c: {head_c}")
    for i in range(4):
        cr = head_r + dr[i]
        cc = head_c + dc[i]
        if 0 <= cr < N and 0 <= cc < N and (grounds[cr][cc] == 4 or grounds[cr][cc] == 3):
            # print(f"head_r: {head_r}, head_c: {head_c}, cr: {cr}, cc: {cc}")
            # grounds[head_r][head_c] = 2
            grounds[cr][cc] = 1
            temp_list.insert(0, [cr, cc])

    # 꼬리 수정
    tail_r, tail_c = temp_list.pop()
    # print(f"tail_r: {tail_r}, tail_c, {tail_c}")
    # print(f"temp_list: {temp_list}")
    for i in range(4):
        cr = tail_r + dr[i]
        cc = tail_c + dc[i]
        if 0 <= cr < N and 0 <= cc < N and grounds[cr][cc] == 2:
            if grounds[tail_r][tail_c] == 3:
                grounds[tail_r][tail_c] = 4
            grounds[cr][cc] = 3
            # print(f"cr: {cr}, cc: {cc}, tail_r: {tail_r}, tail_c: {tail_c}")

    grounds[head_r][head_c] = 2

    return


def change_head_tail(temp_list):
    # print(f"temp_list: {temp_list}")
    before_head_r, before_head_c = temp_list[0]
    before_tail_r, before_tail_c = temp_list[-1]
    temp_list = temp_list[::-1]
    grounds[before_head_r][before_head_c] = 3
    grounds[before_tail_r][before_tail_c] = 1
    return temp_list


def get_score(temp_r, temp_c):
    if grounds[temp_r][temp_c] == 1:
        return 1
    elif grounds[temp_r][temp_c] == 3:
        for i in range(len(teams)):
            if [find_r, find_c] in teams[i]:
                return len(teams[i])
    queue = [[temp_r, temp_c, 1]]
    visited = [[0] * N for _ in range(N)]
    visited[temp_r][temp_c] = 1
    while queue:
        qr, qc, qdis = queue.pop(0)
        for i in range(4):
            cr = qr + dr[i]
            cc = qc + dc[i]
            if 0 <= cr < N and 0 <= cc < N and 0 < grounds[cr][cc] < 3 and visited[cr][cc] == 0:
                visited[cr][cc] = 1
                queue.append([cr, cc, qdis + 1])
                if grounds[cr][cc] == 1:
                    # print(f"cr: {cr}, cc: {cc}, dis: {qdis + 1}")
                    return qdis + 1

    return 0


# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, M, K = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]
teams = list()
total_score = 0

for gr in grounds:
    print(gr)
print()

# 팀 리스트 구하기
for r in range(N):
    for c in range(N):
        if grounds[r][c] == 1:
            temp_list = [[r, c]]
            queue = [[r, c]]
            visited = [[0] * N for _ in range(N)]
            visited[r][c] = 1
            temp_tail_r = -1
            temp_tail_c = -1
            while queue:
                qr, qc = queue.pop(0)
                for i in range(4):
                    cr = qr + dr[i]
                    cc = qc + dc[i]
                    if 0 <= cr < N and 0 <= cc < N and visited[cr][cc] == 0:
                        if 0 < grounds[cr][cc] < 3:
                            visited[cr][cc] = 1
                            temp_list.append([cr, cc])
                            queue.append([cr, cc])
                        elif grounds[cr][cc] == 3:
                            temp_tail_r, temp_tail_c = cr, cc

            temp_list.append([temp_tail_r, temp_tail_c])

            teams.append(temp_list)


# print('move')
# for te in teams:
#     move(te)

# print('change')
# for i in range(len(teams)):
#     teams[i] = change_head_tail(teams[i])

# 현재 공이 던져지는 방향은 우측
cur_direction = 3
cur_r = 0
cur_c = 0
for idx_K in range(K):
    # 1. 각 팀은 머리사람을 따라서 한 칸 이동
    for te in teams:
        move(te)

    # for gr in grounds:
    #     print(gr)

    # 2. 각 라운드마다 공이 정해진 선을 따라 던져진다.
    find_r = -1
    find_c = -1
    queue = [[cur_r, cur_c]]
    # 그 자리에서 찾았다면
    if 0 < grounds[cur_r][cur_c] < 4:
        find_r = cur_r
        find_c = cur_c
    else:
        while queue:
            qr, qc = queue.pop(0)
            cr = qr + dr[cur_direction]
            cc = qc + dc[cur_direction]
            if 0 <= cr < N and 0 <= cc < N:
                # 아직 못만남
                if grounds[cr][cc] == 0 or grounds[cr][cc] == 4:
                    queue.append([cr, cc])
                # 만남
                else:
                    find_r = cr
                    find_c = cc
                    break
    print(f"cur_r: {cur_r}, cur_c: {cur_c}")
    # 다음 반복문을 위해 이동
    round_direction = (cur_direction - 1) % 4
    temp_r = cur_r + dr[round_direction]
    temp_c = cur_c + dc[round_direction]
    # 이동 이후 범위 안에 있다면
    if 0 <= temp_r < N and 0 <= temp_c < N:
        cur_r = temp_r
        cur_c = temp_c
    # 범위 밖이라면 방향만 변경
    else:
        cur_direction = (cur_direction + 1) % 4


    # 찾았다면
    if find_r != -1:
        cur_score = get_score(find_r, find_c)
        total_score += (cur_score ** 2)
        print(f"cur_score: {cur_score, cur_score ** 2}")
        # 찾은 팀의 꼬리와 머리 바꾸어야 함
        for i in range(len(teams)):
            if [find_r, find_c] in teams[i]:
                teams[i] = change_head_tail(teams[i])
                break

    print(f"{idx_K + 1}번째, total_score: {total_score}, find_r: {find_r}, find_c: {find_c}")
    for gr in grounds:
        print(gr)
    print()

print(total_score)

"""
예제 3 틀렸습니다.
7 3 5
3 2 1 0 0 0 0
4 0 4 0 2 1 4
4 4 4 0 2 0 4
0 0 0 0 3 4 4
2 1 3 2 0 0 0
2 0 0 2 0 0 0
2 2 2 2 0 0 0

현지 조건에서는 1, 3 안붙어있었음
코드트리를 위해 코드 수정
get_score에서 1(머리) 만났을 때 로직 수정
get_score에서 맨 마지막에 return 0 추가

예제 4 틀렸습니다.
get_score에서 3(꼬리) 만났을 때 로직 수정
"""