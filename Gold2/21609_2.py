import sys

sys.stdin = open('BJ/test.txt', 'r')

# 21609 상어 중학교

def gravity():
    for c in range(N):
        for r in range(N - 2, -1, -1):
            # print(f"r: {r}, c: {c}")
            # 아래가 빈 칸이고 현재 칸이 -1이 아니라면
            if grounds[r + 1][c] == -2 and grounds[r][c] != -1:
                # 현재 r
                temp_r = r
                while temp_r + 1 < N and grounds[temp_r + 1][c] == -2:
                    # print(temp_r, temp_r + 1)
                    temp_block = grounds[temp_r][c]
                    grounds[temp_r][c] = grounds[temp_r + 1][c]
                    grounds[temp_r + 1][c] = temp_block
                    temp_r += 1
    return
    # print('after')
    # for gr in grounds:
    #     print(gr)


def rotate90():
    temp_grounds = [gr[:] for gr in grounds]
    for r in range(N):
        for c in range(N):
            grounds[N - 1 - c][r] = temp_grounds[r][c]
    return


# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, M = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]
total_score = 0

# print('init')
# for gr in grounds:
#     print(gr)

# 조건 맞을 때까지 계속 진행
while True:
    visited = [[0] * N for _ in range(N)]
    maximum_list = list()
    maximum_rainbow = 0
    for r in range(N):
        for c in range(N):
            temp_list = [[r, c]]
            cur_num = grounds[r][c]
            rainbow = 0
            rainbow_grounds = list()
            # 검은 블록이나 무지개 블록이나 빈 공간이면 continue
            if cur_num == -1 or cur_num == 0 or cur_num == -2:
                continue
            visited[r][c] = cur_num
            queue = [[r, c]]
            while queue:
                qr, qc = queue.pop(0)
                for i in range(4):
                    cr = qr + dr[i]
                    cc = qc + dc[i]
                    if 0 <= cr < N and 0 <= cc < N and visited[cr][cc] == 0 and (grounds[cr][cc] == cur_num or grounds[cr][cc] == 0): # or grounds[cr][cc] == 0):
                        queue.append([cr, cc])
                        # 무지개 블록이면
                        if grounds[cr][cc] == 0:
                            rainbow += 1
                            rainbow_grounds.append([cr, cc])
                        visited[cr][cc] = cur_num
                        temp_list.append([cr, cc])

            # 크기가 가장 큰 블록 그룹
            if len(temp_list) > len(maximum_list):
                maximum_list = temp_list[:]
                maximum_rainbow = rainbow
            # 같다면 무지개 블록 수가 가장 많은 블록
            elif len(temp_list) == len(maximum_list) and rainbow >= maximum_rainbow:
                maximum_list = temp_list[:]
                maximum_rainbow = rainbow
            # 기준 행 열 비교 -> rainbow 비교시 등호 넣어서 해결

            # rainbow grounds visited 초기화
            for gr, gc in rainbow_grounds:
                visited[gr][gc] = 0
    # print(f"maximum_list: {maximum_list}")
    # print(f"maximum_rainbow: {maximum_rainbow}")

    # 길이 미달이면 break
    if len(maximum_list) < 2:
        break

    # 점수 더해주기
    total_score += (len(maximum_list) ** 2)
    # print(f"total_score: {total_score}")
    # 연산에 사용한 것들 없애기
    for mr, mc in maximum_list:
        grounds[mr][mc] = -2
    # print('calc')
    # for gr in grounds:
    #     print(gr)
    # 중력
    gravity()

    # print('after gravity')
    # for gr in grounds:
    #     print(gr)
    # 반시계 90
    rotate90()

    # print('after rotate')
    # for gr in grounds:
    #     print(gr)
    # 중력
    gravity()
    # print('after gravity 2')
    # for gr in grounds:
    #     print(gr)

    # break

print(total_score)
