import sys

sys.stdin = open('BJ/test.txt', 'r')

# 23291 어항 정리

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, K = map(int, input().split())
fishes = list(map(int, input().split()))
result = 0

while True:
    # 물고기 수가 가장 적은 어항에 물고기 한 마리를 넣는다.
    minimum = min(fishes)
    for i in range(len(fishes)):
        if fishes[i] == minimum:
            fishes[i] += 1

    # 어항을 쌓는다.

    fish_list = list()
    for fish in fishes:
        fish_list.append([fish])

    # 가장 왼쪽 어항을 그 어항의 오른쪽 어항 위에 올려놓는다.
    left_fish = fish_list.pop(0)
    fish_list[0].extend(left_fish)

    # 2개 이상 쌓여있는 어항 모두 공중부양
    length = 0
    for i in range(len(fish_list)):
        if len(fish_list[i]) >= 2:
            length += 1

    while len(fish_list) - length >= len(fish_list[0]):
        up_fish = list()
        for i in range(length):
            my_fishes = fish_list.pop(0)
            up_fish.append(my_fishes)

        up_fish_90 = list()
        for c in range(len(up_fish[0])):
            temp = list()
            for r in range(len(up_fish) -1, -1, -1):
                temp.append(up_fish[r][c])
            up_fish_90.append(temp)

        for i in range(len(up_fish_90)):
            fish_list[i].extend(up_fish_90[i])

        # 2개 이상 쌓여있는 어항 모두 공중부양
        length = 0
        for i in range(len(fish_list)):
            if len(fish_list[i]) >= 2:
                length += 1

    # 인접 어항 연산 위해 직사각형 꼴로 만들어주기
    calc_fish = list()
    maximum = len(fish_list[0])
    for i in range(len(fish_list)):
        if len(fish_list[i]) == maximum:
            calc_fish.append(fish_list[i])
        else:
            calc_fish.append(fish_list[i] + [0] * (maximum - len(fish_list[i])))

    r_length = len(calc_fish)
    c_length = len(calc_fish[0])
    visited = [[0] * c_length for _ in range(r_length)]
    temp_calc_list = [[0] * c_length for _ in range(r_length)]
    for r in range(r_length):
        for c in range(c_length):
            visited[r][c] = 1
            if calc_fish[r][c] == 0:
                continue
            for i in range(4):
                cr = r + dr[i]
                cc = c + dc[i]
                # 범위 안에 있으면서 방문하지 않은 곳이라면
                if 0 <= cr < r_length and 0 <= cc < c_length and visited[cr][cc] == 0:
                    if calc_fish[cr][cc] == 0:
                        continue
                    diff = abs(calc_fish[r][c] - calc_fish[cr][cc])
                    diff //= 5
                    if calc_fish[r][c] > calc_fish[cr][cc]:
                        temp_calc_list[r][c] -= diff
                        temp_calc_list[cr][cc] += diff
                    elif calc_fish[r][c] < calc_fish[cr][cc]:
                        temp_calc_list[r][c] += diff
                        temp_calc_list[cr][cc] -= diff

    for r in range(r_length):
        for c in range(c_length):
            calc_fish[r][c] += temp_calc_list[r][c]

    # 다시 어항을 바닥에 일렬로
    fish_list = list()
    for r in range(r_length):
        for c in range(c_length):
            if calc_fish[r][c] > 0:
                fish_list.append([calc_fish[r][c]])

    # 왼쪽 N / 2개를 180도 회전시켜서 위에 놓기
    length = len(fish_list) // 2
    up_fish = fish_list[:length]
    for _ in range(length):
        fish_list.pop(0)

    for i in range(length):
        fish_list[i].extend(up_fish[length - 1 - i][::-1])

    # 왼쪽 N / 4개를 180도 회전시켜서 위에 놓기
    length = len(fish_list) // 2
    up_fish = fish_list[:length]
    for _ in range(length):
        fish_list.pop(0)

    for i in range(length):
        fish_list[i].extend(up_fish[length - 1 - i][::-1])

    # 물고기 조절 작업 다시
    calc_fish = [fi[:] for fi in fish_list]

    r_length = len(calc_fish)
    c_length = len(calc_fish[0])
    # print(f"r_length: {r_length}, c_length: {c_length}")
    visited = [[0] * c_length for _ in range(r_length)]
    temp_calc_list = [[0] * c_length for _ in range(r_length)]
    for r in range(r_length):
        for c in range(c_length):
            visited[r][c] = 1
            if calc_fish[r][c] == 0:
                continue
            for i in range(4):
                cr = r + dr[i]
                cc = c + dc[i]
                # 범위 안에 있으면서 방문하지 않은 곳이라면
                if 0 <= cr < r_length and 0 <= cc < c_length and visited[cr][cc] == 0:
                    if calc_fish[cr][cc] == 0:
                        continue
                    diff = abs(calc_fish[r][c] - calc_fish[cr][cc])
                    diff //= 5
                    if calc_fish[r][c] > calc_fish[cr][cc]:
                        temp_calc_list[r][c] -= diff
                        temp_calc_list[cr][cc] += diff
                    elif calc_fish[r][c] < calc_fish[cr][cc]:
                        temp_calc_list[r][c] += diff
                        temp_calc_list[cr][cc] -= diff

    for r in range(r_length):
        for c in range(c_length):
            calc_fish[r][c] += temp_calc_list[r][c]

    fishes = list()
    for ca in calc_fish:
        fishes.extend(ca)

    result += 1

    if max(fishes) - min(fishes) <= K:
        break

print(result)
