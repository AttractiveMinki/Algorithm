# 2*2 matrix에서 시계/반시계 방향으로 돌리기

my_matrix = [[0, 1], [2, 3]]

temp_matrix = [my[:] for my in my_matrix]

# 반시계방향 90도
for r in range(len(my_matrix)):
    for c in range(len(my_matrix[0])):
        # print(r, c, '--', c, len(my_matrix) - 1 - r)
        my_matrix[r][c] = temp_matrix[c][len(my_matrix) - 1 - r]

for my in my_matrix:
    print(my)
    # [1, 3]
    # [0, 2]

# 시계방향 90도 (반시계방향일때의 my_matrix와 temp_matrix의 index를 맞바꾸면 된다.)
for r in range(len(my_matrix)):
    for c in range(len(my_matrix[0])):
        # print(r, c, '--', c, len(my_matrix) - 1 - r)
        my_matrix[c][len(my_matrix) - 1 - r] = temp_matrix[r][c]

for my in my_matrix:
    print(my)
    # [2, 0]
    # [3, 1]


# 특수한 케이스 - 격자를 만들고 격자 내에서 시계방향 90도 (백준 20058 - 마법사 상어와 파이어볼)

N = 3 # 8 * 8 matrix
my_matrix = [[1] * 6 + [2] * 2 for _ in range(8)]
# L = list(map(int, input().split()))
L = [1]

for magic_num in L:
    for r in range(0, 2 ** N, 2 ** magic_num):
        for c in range(0, 2 ** N, 2 ** magic_num):
            
            # 격자 안에서 탐색하며 시계방향으로 90도 회전
            for tr in range(r, r + 2 ** magic_num):
                for tc in range(c, c + 2 ** magic_num):
                    # r값은 tc - (c - r)
                    # c값은 (r + c + length(2 ** magic_num) - 1) - tr
                    my_matrix[tc - (c - r)][(r + c + 2 ** magic_num - 1) - tr] = my_matrix[tr][tc]

for my in my_matrix:
    print(my)
    # [1, 1, 1, 1, 1, 1, 2, 2]
    # [1, 1, 1, 1, 1, 1, 2, 2]
    # [1, 1, 1, 1, 1, 1, 2, 2]
    # [1, 1, 1, 1, 1, 1, 2, 2]
    # [1, 1, 1, 1, 1, 1, 2, 2]
    # [1, 1, 1, 1, 1, 1, 2, 2]
    # [1, 1, 1, 1, 1, 1, 2, 2]
    # [1, 1, 1, 1, 1, 1, 2, 2]
