import sys

sys.stdin = open('BJ/test.txt', 'r')

# 14891 톱니바퀴

# 반시계방향
def anti_clock(rounds, visited, idx):
    temp_rounds = [rou[:] for rou in rounds[idx]]
    visited[idx] = 1

    rounds[idx][0][0] = temp_rounds[0][1]
    rounds[idx][0][1] = temp_rounds[0][2]
    rounds[idx][0][2] = temp_rounds[1][2]
    rounds[idx][1][2] = temp_rounds[2][2]
    rounds[idx][2][2] = temp_rounds[2][1]
    rounds[idx][2][1] = temp_rounds[2][0]
    rounds[idx][2][0] = temp_rounds[1][0]
    rounds[idx][1][0] = temp_rounds[0][0]

    # 왼쪽 체크
    if idx - 1 >= 0 and visited[idx - 1] == 0:
        # 조건이 맞다면 돌려주기
        if rounds[idx - 1][1][2] != temp_rounds[1][0]:
            clock(rounds, visited, idx - 1)

    # 오른쪽 체크
    if idx + 1 < 4 and visited[idx + 1] == 0:
        # 조건이 맞다면 돌려주기
        if temp_rounds[1][2] != rounds[idx + 1][1][0]:
            clock(rounds, visited, idx + 1)

    return rounds


# 시계방향
def clock(rounds, visited, idx):
    temp_rounds = [rou[:] for rou in rounds[idx]]
    visited[idx] = 1

    rounds[idx][0][2] = temp_rounds[0][1]
    rounds[idx][1][2] = temp_rounds[0][2]
    rounds[idx][2][2] = temp_rounds[1][2]
    rounds[idx][2][1] = temp_rounds[2][2]
    rounds[idx][2][0] = temp_rounds[2][1]
    rounds[idx][1][0] = temp_rounds[2][0]
    rounds[idx][0][0] = temp_rounds[1][0]
    rounds[idx][0][1] = temp_rounds[0][0]

    # 왼쪽 체크
    if idx - 1 >= 0 and visited[idx - 1] == 0:
        # 조건이 맞다면 돌려주기
        if rounds[idx - 1][1][2] != temp_rounds[1][0]:
            anti_clock(rounds, visited, idx - 1)

    # 오른쪽 체크
    if idx + 1 < 4 and visited[idx + 1] == 0:
        # 조건이 맞다면 돌려주기
        if temp_rounds[1][2] != rounds[idx + 1][1][0]:
            anti_clock(rounds, visited, idx + 1)

    return rounds

rounds = list()
rounds.append([[0 for _ in range(3)] for _ in range(3)])
rounds.append([[0 for _ in range(3)] for _ in range(3)])
rounds.append([[0 for _ in range(3)] for _ in range(3)])
rounds.append([[0 for _ in range(3)] for _ in range(3)])

numbers1 = input()
rounds[0][0][1] = int(numbers1[0])
rounds[0][0][2] = int(numbers1[1])
rounds[0][1][2] = int(numbers1[2])
rounds[0][2][2] = int(numbers1[3])
rounds[0][2][1] = int(numbers1[4])
rounds[0][2][0] = int(numbers1[5])
rounds[0][1][0] = int(numbers1[6])
rounds[0][0][0] = int(numbers1[7])

numbers2 = input()
rounds[1][0][1] = int(numbers2[0])
rounds[1][0][2] = int(numbers2[1])
rounds[1][1][2] = int(numbers2[2])
rounds[1][2][2] = int(numbers2[3])
rounds[1][2][1] = int(numbers2[4])
rounds[1][2][0] = int(numbers2[5])
rounds[1][1][0] = int(numbers2[6])
rounds[1][0][0] = int(numbers2[7])

numbers3 = input()
rounds[2][0][1] = int(numbers3[0])
rounds[2][0][2] = int(numbers3[1])
rounds[2][1][2] = int(numbers3[2])
rounds[2][2][2] = int(numbers3[3])
rounds[2][2][1] = int(numbers3[4])
rounds[2][2][0] = int(numbers3[5])
rounds[2][1][0] = int(numbers3[6])
rounds[2][0][0] = int(numbers3[7])

numbers4 = input()
rounds[3][0][1] = int(numbers4[0])
rounds[3][0][2] = int(numbers4[1])
rounds[3][1][2] = int(numbers4[2])
rounds[3][2][2] = int(numbers4[3])
rounds[3][2][1] = int(numbers4[4])
rounds[3][2][0] = int(numbers4[5])
rounds[3][1][0] = int(numbers4[6])
rounds[3][0][0] = int(numbers4[7])


K = int(input())
for _ in range(K):
    num_round, direction = map(int, input().split())

    # 시계 방향
    if direction == 1:
        # 1번
        if num_round == 1:
            rounds = clock(rounds, [0, 0, 0, 0], 0)
        elif num_round == 2:
            rounds = clock(rounds, [0, 0, 0, 0], 1)
        elif num_round == 3:
            rounds = clock(rounds, [0, 0, 0, 0], 2)
        elif num_round == 4:
            rounds = clock(rounds, [0, 0, 0, 0], 3)

    elif direction == -1:
        if num_round == 1:
            rounds = anti_clock(rounds, [0, 0, 0, 0], 0)
        elif num_round == 2:
            rounds = anti_clock(rounds, [0, 0, 0, 0], 1)
        elif num_round == 3:
            rounds = anti_clock(rounds, [0, 0, 0, 0], 2)
        elif num_round == 4:
            rounds = anti_clock(rounds, [0, 0, 0, 0], 3)


score = 0
if rounds[0][0][1] == 1:
    score += 1

if rounds[1][0][1] == 1:
    score += 2

if rounds[2][0][1] == 1:
    score += 4

if rounds[3][0][1] == 1:
    score += 8


print(score)
