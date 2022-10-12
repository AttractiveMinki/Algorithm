import sys

sys.stdin = open('BJ/test.txt', 'r')

# 21608 상어 초등학교

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N = int(input())
likes = [list(map(int, input().split())) for _ in range(N ** 2)]
grounds = [[0] * N for _ in range(N)]

# for li in likes:
#     print(li)
# print('-===')
# for gr in grounds:
#     print(gr)

score_help = dict()
# 자리 구하기
for idx in range(N ** 2):
    cur_likes = likes[idx]
    cur_student = cur_likes.pop(0)

    # 좋아하는 학생이 인접
    # 빈 자리가 많아야
    like_student = 0
    empty_seat = 0
    result_r = -1
    result_c = -1

    for r in range(N):
        for c in range(N):
            if grounds[r][c] == 0:
                temp_student = 0
                temp_empty = 0
                for i in range(4):
                    cr = r + dr[i]
                    cc = c + dc[i]
                    if 0 <= cr < N and 0 <= cc < N:
                        if grounds[cr][cc] in cur_likes:
                            temp_student += 1
                        elif grounds[cr][cc] == 0:
                            temp_empty += 1
                if temp_student > like_student:
                    like_student = temp_student
                    empty_seat = temp_empty
                    result_r = r
                    result_c = c
                    # print(f"1 r: {r}. c: {c}, result_r: {result_r}, result_c: {result_c}, temp_empty: {temp_empty}, empty_seat: {empty_seat}")
                elif temp_student == like_student and temp_empty > empty_seat:
                    empty_seat = temp_empty
                    result_r = r
                    result_c = c
                    # print(f"2 r: {r}. c: {c}, result_r: {result_r}, result_c: {result_c}, temp_empty: {temp_empty}, empty_seat: {empty_seat}")
                elif result_r == -1 and result_c == -1:
                    result_r = r
                    result_c = c
    #                 print(f"3 r: {r}. c: {c}, result_r: {result_r}, result_c: {result_c}, temp_empty: {temp_empty}, empty_seat: {empty_seat}")
    # print(f"cur_student: {cur_student}, result_r: {result_r}, result_c: {result_c}")
    # print(f"like_student: {like_student}, empty_seat: {empty_seat}")
    grounds[result_r][result_c] = cur_student
    score_help[cur_student] = cur_likes

# print(score_help)

# for gr in grounds:
#     print(gr)

# score 구하기
result = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for i in range(4):
            cr = r + dr[i]
            cc = c + dc[i]
            if 0 <= cr < N and 0 <= cc < N and grounds[cr][cc] in score_help[grounds[r][c]]:
                # print(grounds[cr][cc], score_help[grounds[r][c]], r, c)
                cnt += 1
        # print(f"cnt: {cnt}")
        if cnt == 0:
            continue
        cnt -= 1

        result += (10 ** cnt)

print(result)
