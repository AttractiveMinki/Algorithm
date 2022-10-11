import sys

sys.stdin = open('BJ/test.txt', 'r')

# 20057 마법사 상어와 토네이도

# 좌 하 우 상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def tornado(cur_r, cur_c, cur_dir):
    plus_gr = list()
    cur_dust = grounds[cur_r][cur_c]
    total_spend_dust = 0
    total_outside_dust = 0
    # print(f"cur_r: {cur_r}, cur_c: {cur_c}")

    ## 5% 앞앞 ##
    go_two_r = cur_r + (dr[cur_dir]) * 2
    go_two_c = cur_c + (dc[cur_dir]) * 2
    dust = cur_dust * 5 // 100
    # 범위 안에 있다면
    if 0 <= go_two_r < N and 0 <= go_two_c < N:
        total_spend_dust += dust
        plus_gr.append([go_two_r, go_two_c, dust])
        # print(f"1 r: {go_two_r}, c: {go_two_c}, {plus_gr[go_two_r][go_two_c]}")
    # 범위 밖이라면
    else:
        total_outside_dust += dust

    ## 10% 앞 왼쪽 ##
    go_one_r = cur_r + dr[cur_dir]
    go_one_c = cur_c + dc[cur_dir]

    # 좌 -> 아래로
    cur_dir2 = (cur_dir + 1) % 4
    go_left_r = go_one_r + dr[cur_dir2]
    go_left_c = go_one_c + dc[cur_dir2]
    dust = cur_dust * 10 // 100
    # 범위 안에 있다면
    if 0 <= go_left_r < N and 0 <= go_left_c < N:
        total_spend_dust += dust
        plus_gr.append([go_left_r, go_left_c, dust])
        # print(f"2 r: {go_left_r}, c: {go_left_c}, {plus_gr[go_left_r][go_left_c]}")
        # print(f"cur_r: {cur_r}, cur_c: {cur_c}, go_one_r: {go_one_r}, go_one_c: {go_one_c}")
    # 범위 밖이라면
    else:
        total_outside_dust += dust

    ## 10% 앞 오른쪽 ##
    # 우 -> 위로
    cur_dir2 = (cur_dir - 1) % 4
    go_right_r = go_one_r + dr[cur_dir2]
    go_right_c = go_one_c + dc[cur_dir2]
    dust = cur_dust * 10 // 100
    # 범위 안에 있다면
    if 0 <= go_right_r < N and 0 <= go_right_c < N:
        total_spend_dust += dust
        plus_gr.append([go_right_r, go_right_c, dust])
        # print(f"3 r: {go_right_r}, c: {go_right_c}, {plus_gr[go_right_r][go_right_c]}")
    # 범위 밖이라면
    else:
        total_outside_dust += dust

    ## 7% 왼쪽 ##
    cur_dir2 = (cur_dir + 1) % 4
    go_left_r = cur_r + dr[cur_dir2]
    go_left_c = cur_c + dc[cur_dir2]
    dust = cur_dust * 7 // 100
    # 범위 안에 있다면
    if 0 <= go_left_r < N and 0 <= go_left_c < N:
        total_spend_dust += dust
        plus_gr.append([go_left_r, go_left_c, dust])
        # print(f"4 r: {go_left_r}, c: {go_left_c}, {plus_gr[go_left_r][go_left_c]}")
    # 범위 밖이라면
    else:
        total_outside_dust += dust

    ## 2% 왼왼쪽 ##
    go_left_left_r = cur_r + (dr[cur_dir2] * 2)
    go_left_left_c = cur_c + (dc[cur_dir2] * 2)
    dust = cur_dust * 2 // 100
    # 범위 안에 있다면
    if 0 <= go_left_left_r < N and 0 <= go_left_left_c < N:
        total_spend_dust += dust
        plus_gr.append([go_left_left_r, go_left_left_c, dust])
        # print(f"5 r: {go_left_left_r}, c: {go_left_left_c}, {plus_gr[go_left_left_r][go_left_left_c]}")
    # 범위 밖이라면
    else:
        total_outside_dust += dust

    ## 1% 왼쪽의 왼쪽 ##
    cur_dir2 = (cur_dir2 + 1) % 4
    go_left_r = go_left_r + dr[cur_dir2]
    go_left_c = go_left_c + dc[cur_dir2]
    dust = cur_dust * 1 // 100
    # 범위 안에 있다면
    if 0 <= go_left_r < N and 0 <= go_left_c < N:
        total_spend_dust += dust
        plus_gr.append([go_left_r, go_left_c, dust])
    # 범위 밖이라면
    else:
        total_outside_dust += dust

    ## 7% 오른쪽 ##
    cur_dir2 = (cur_dir - 1) % 4
    go_right_r = cur_r + dr[cur_dir2]
    go_right_c = cur_c + dc[cur_dir2]
    dust = cur_dust * 7 // 100
    # 범위 안에 있다면
    if 0 <= go_right_r < N and 0 <= go_right_c < N:
        total_spend_dust += dust
        plus_gr.append([go_right_r, go_right_c, dust])
    # 범위 밖이라면
    else:
        total_outside_dust += dust

    ## 2% 오른오른쪽 ##
    go_right_right_r = cur_r + (dr[cur_dir2] * 2)
    go_right_right_c = cur_c + (dc[cur_dir2] * 2)
    dust = cur_dust * 2 // 100
    # 범위 안에 있다면
    if 0 <= go_right_right_r < N and 0 <= go_right_right_c < N:
        total_spend_dust += dust
        plus_gr.append([go_right_right_r, go_right_right_c, dust])
    # 범위 밖이라면
    else:
        total_outside_dust += dust

    ## 1% 오른쪽의 오른쪽 ##
    cur_dir2 = (cur_dir2 - 1) % 4
    go_right_r = go_right_r + dr[cur_dir2]
    go_right_c = go_right_c + dc[cur_dir2]
    dust = cur_dust * 1 // 100
    # 범위 안에 있다면
    if 0 <= go_right_r < N and 0 <= go_right_c < N:
        total_spend_dust += dust
        plus_gr.append([go_right_r, go_right_c, dust])
    # 범위 밖이라면
    else:
        total_outside_dust += dust

    # y값의 먼지 없애기
    grounds[cur_r][cur_c] = 0

    # alpha 구하기
    alpha = cur_dust - total_spend_dust - total_outside_dust
    # print(
    #     f"alpha: {alpha}, cur_dust: {cur_dust}, total_spend_dust: {total_spend_dust}, total_outside_dust: {total_outside_dust}")

    cr = cur_r + dr[cur_dir]
    cc = cur_c + dc[cur_dir]
    # 범위 안에 있다면
    if 0 <= cr < N and 0 <= cc < N:
        plus_gr.append([cr, cc, alpha])
        # print("범위 안")
    else:
        total_outside_dust += alpha
        alpha = 0
        # print('범위 밖')

    # print(f"alpha: {alpha}, cur_dust: {cur_dust}, total_spend_dust: {total_spend_dust}, total_outside_dust: {total_outside_dust}")
    # 각 칸에 dust 더해주기
    for temp_r, temp_c, temp_dust in plus_gr:
        grounds[temp_r][temp_c] += temp_dust
    # print('--', 'plus')
    # for pl in plus_gr:
    #     print(pl)


    return total_outside_dust



N = int(input())
grounds = [list(map(int, input().split())) for _ in range(N)]
result = 0

cur_r = N // 2
cur_c = N // 2
cur_dir = 0
cur_cnt = 1
while cur_c >= 0:
    for _ in range(cur_cnt):
        # 좌/우
        cur_r = cur_r + dr[cur_dir]
        cur_c = cur_c + dc[cur_dir]
        if cur_c < 0:
            break

        cur_score = tornado(cur_r, cur_c, cur_dir)
        result += cur_score
        # print('==')
        # for gr in grounds:
        #     print(gr)
        # print(f"result: {result}")
    if cur_c < 0:
        break

    cur_dir = (cur_dir + 1) % 4

    for _ in range(cur_cnt):
        # 하/상
        cur_r = cur_r + dr[cur_dir]
        cur_c = cur_c + dc[cur_dir]
        if cur_c < 0:
            break

        cur_score = tornado(cur_r, cur_c, cur_dir)
        result += cur_score
        # print('==')
        # for gr in grounds:
        #     print(gr)
        # print(f"result: {result}")

    if cur_c < 0:
        break

    cur_dir = (cur_dir + 1) % 4

    # 횟수 증가
    cur_cnt += 1

print(result)

"""
시간 초과
plus_gr을 넣어줄 때, N * N 배열로 만들어주니 시간초과가 났다.
맞왜틀의 연속.. 의심..
찾다찾다 못찾아서, 예전에 맞춘 기록과 시간초과가 났던 기록을 비교했다.
plus_gr을 초기화시켜서 받는 게 아니라, 해당하는 r, c값이 나오면 그 r, c 값과 dust 값을 따로 저장해주는 방식을 사용했다.
아.... 똑같이 틀렸던 것을 또 틀렸다. 흑흑

"""