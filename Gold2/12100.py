import sys

sys.stdin = open('test.txt', 'r')

# 12100 2048 (Easy)

def lets_move(move_num):
    # 상
    if move_num == 0:
        # 위로 땡기면서 빈 칸 채우기
        for c in range(N):
            for r in range(N):
                if temp_blocks[r][c] == 0:
                    temp_r = r
                    while N - 1 > temp_r and temp_blocks[temp_r][c] == 0:
                        temp_r += 1
                    temp_blocks[r][c] = temp_blocks[temp_r][c]
                    temp_blocks[temp_r][c] = 0

        for c in range(N):
            for r in range(N - 1):
                # 아래 칸과 같다면 2배 해주기
                if temp_blocks[r][c] == temp_blocks[r + 1][c]:
                    temp_blocks[r][c] *= 2
                    temp_blocks[r + 1][c] = 0 # 아래 for문에 못들어가는 상황 방지
                    # 위로 한 칸씩 땡기기
                    for temp_r in range(r + 1, N - 1):
                        temp_blocks[temp_r][c] = temp_blocks[temp_r + 1][c]
                        temp_blocks[temp_r + 1][c] = 0

    # 좌
    elif move_num == 1:
        # 왼쪽으로 땡기면서 빈 칸 채우기
        for r in range(N):
            for c in range(N):
                if temp_blocks[r][c] == 0:
                    temp_c = c
                    while N - 1 > temp_c and temp_blocks[r][temp_c] == 0:
                        temp_c += 1
                    temp_blocks[r][c] = temp_blocks[r][temp_c]
                    temp_blocks[r][temp_c] = 0

        for r in range(N):
            for c in range(N - 1):
                # 오른쪽 칸과 같다면 2배 해주기
                if temp_blocks[r][c] == temp_blocks[r][c + 1]:
                    temp_blocks[r][c] *= 2
                    temp_blocks[r][c + 1] = 0
                    # 왼쪽으로 한 칸씩 땡기기
                    for temp_c in range(c + 1, N - 1):
                        temp_blocks[r][temp_c] = temp_blocks[r][temp_c + 1]
                        temp_blocks[r][temp_c + 1] = 0

    # 하
    elif move_num == 2:
        # 아래로 땡기면서 빈 칸 채우기
        for c in range(N):
            for r in range(N - 1, -1, -1):
                if temp_blocks[r][c] == 0:
                    temp_r = r
                    while temp_r > 0 and temp_blocks[temp_r][c] == 0:
                        temp_r -= 1
                    temp_blocks[r][c] = temp_blocks[temp_r][c]
                    temp_blocks[temp_r][c] = 0

        for c in range(N):
            for r in range(N - 1, -1, -1): # ValueError: range() arg 3 must not be zero
                # r == 0이면 안봐도 됨
                if r == 0:
                    break

                # 위 칸과 같다면 2배 해주기
                if temp_blocks[r][c] == temp_blocks[r - 1][c]:
                    temp_blocks[r][c] *= 2
                    temp_blocks[r - 1][c] = 0
                    # 아래로 한 칸씩 땡기기
                    for temp_r in range(r - 1, -1, -1):
                        if temp_r == 0:
                            break
                        temp_blocks[temp_r][c] = temp_blocks[temp_r - 1][c]
                        temp_blocks[temp_r - 1][c] = 0

    # 우
    elif move_num == 3:
        # 오른쪽으로 땡기면서 빈 칸 채우기
        for r in range(N):
            for c in range(N - 1, -1, -1):
                if temp_blocks[r][c] == 0:
                    temp_c = c
                    while temp_c > 0 and temp_blocks[r][temp_c] == 0:
                        temp_c -= 1
                    temp_blocks[r][c] = temp_blocks[r][temp_c]
                    temp_blocks[r][temp_c] = 0

        for r in range(N):
            for c in range(N - 1, -1, -1):
                # c == 0이면 안봐도 됨
                if c == 0:
                    break

                # 왼쪽 칸과 같다면 2배 해주기
                if temp_blocks[r][c] == temp_blocks[r][c - 1]:
                    temp_blocks[r][c] *= 2
                    temp_blocks[r][c - 1] = 0
                    # 오른쪽으로 한 칸씩 땡기기
                    for temp_c in range(c - 1, -1, -1):
                        if temp_c == 0:
                            break
                        temp_blocks[r][temp_c] = temp_blocks[r][temp_c - 1]
                        temp_blocks[r][temp_c - 1] = 0


# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]

maximum = 0
for idx in range(4 ** 5): # 4 ** 5
    temp_blocks = [bl[:] for bl in blocks]
    first_move = (idx // (4 ** 4)) % 4
    second_move = (idx // (4 ** 3)) % 4
    third_move = (idx // (4 ** 2)) % 4
    fourth_move = (idx // (4 ** 1)) % 4
    fifth_move = idx % 4

    # 첫 번째 움직임
    lets_move(first_move)

    # 두 번째 움직임
    lets_move(second_move)
    
    # 세 번째 움직임
    lets_move(third_move)

    # 네 번째 움직임
    lets_move(fourth_move)

    # 다섯 번째 움직임
    lets_move(fifth_move)

    maximum = max(max(max(te) for te in temp_blocks), maximum)

print(maximum)
