import sys

sys.stdin = open('./test.txt', 'r')

# 예술성

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
score = 0
# for nu in numbers:
#     print(nu)

# 4번 반복
for _ in range(4):
    # 그룹 만들기
    groups = list()
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                temp_queue = list()
                visited[r][c] = numbers[r][c]
                queue = [[r, c]]
                while queue:
                    cur_r, cur_c = queue.pop(0)
                    temp_queue.append([cur_r, cur_c, numbers[r][c]])
                    for i in range(4):
                        cr = cur_r + dr[i]
                        cc = cur_c + dc[i]
                        if 0 <= cr < N and 0 <= cc < N and visited[cr][cc] == 0 and numbers[r][c] == numbers[cr][cc]:
                            visited[cr][cc] = numbers[cr][cc]
                            queue.append([cr, cc])
                # print('temp_queue')
                # for te in temp_queue:
                #     print(te)
                # print('==')
                groups.append(temp_queue)

    # print('groups')
    # for gr in groups:
    #     print(gr)

    # 그룹 1
    temp_score = 0
    for i in range(len(groups)):
        # 그룹 2
        for j in range(i + 1, len(groups)):
            if i != j:
                find_num = groups[j][0][-1]
                stick_cnt = 0
                # print(groups[i])
                for temp_r, temp_c, _ in groups[i]:
                    for idx in range(4):
                        cr = temp_r + dr[idx]
                        cc = temp_c + dc[idx]
                        # 변 갯수 세기
                        if 0 <= cr < N and 0 <= cc < N and [cr, cc, find_num] in groups[j]:
                            stick_cnt += 1

                temp_score = ((len(groups[i]) + len(groups[j])) * groups[i][0][-1] * find_num * stick_cnt)
                # print(i, j, temp_score)
                # print(f"i: {i}, j: {j}, temp_score: {temp_score}, stick_cnt: {stick_cnt}")

                score += temp_score

    # print('before')
    # for nu in numbers:
    #     print(nu)

    # 회전시키기
    temp_numbers = [nu[:] for nu in numbers]
    # 십자 모양 -> 통째로 반시계 회전
    for r in range(N):
        for c in range(N):
            if r == (N // 2) or c == (N // 2):
                numbers[N - 1 - c][r] = temp_numbers[r][c]
                # print(f"십자 r: {r}. c: {c}, r1: {N - 1 - c}, c1: {r}")
            # 십자 모양 제외한 4개의 정사각형 -> 개별적으로 시계방향으로 90도씩 회전
            else:
                # 위
                if r < N // 2:
                    # 좌
                    if c < N // 2:
                        numbers[r][c] = temp_numbers[((N - 3) // 2) - c][r]
                    # 우
                    else:
                        numbers[r][c] = temp_numbers[N - 1 - c][(N // 2) + 1 + r]
                # 아래
                else:
                    # 좌
                    if c < N // 2:
                        # print(f"r: {r}, c: {c}, r1: {N - 1 - c}, c1: {r - (N // 2) - 1}")
                        numbers[r][c] = temp_numbers[N - 1 - c][r - (N // 2) - 1]
                    # 우
                    else:
                        # 칸수 + N + 1 - c
                        # print(f"r: {r}, c: {c}, r1: {((N - 3) // 2) + N + 1 - c}, c1: {r}")
                        numbers[r][c] = temp_numbers[((N - 3) // 2) + N + 1 - c][r]

                # print(f"r: {r}, c: {c}, r1: {N - 1 - c}, c1: {(N // 2) + 1 + r}")
                # numbers[r][c] = temp_numbers[N - 1 - c][(N // 2) + 1 + r]

    # print('after')
    # for nu in numbers:
    #     print(nu)
print(score)