import sys

sys.stdin = open('BJ/test.txt', 'r')

# 21611 마법사 상어와 블리자드

# 빙글빙글 돌면서 보는 숫자들을 모아 하나의 리스트로 만들어주는 함수
def make_one():
    cur_r = N // 2
    cur_c = N // 2
    cur_dir = 0
    num = 1
    while cur_c >= 0:
        for _ in range(num):
            cur_r += dr[cur_dir]
            cur_c += dc[cur_dir]
            # print(cur_r, cur_c)
            # 범위 밖이면 백트래킹
            if cur_c == -1:
                return
            if grounds[cur_r][cur_c] > 0:
                one_list.append(grounds[cur_r][cur_c])
            # 0이면 백트래킹
            elif grounds[cur_r][cur_c] == 0:
                return
        if cur_dir % 2 == 1:
            num += 1

        cur_dir = (cur_dir + 1) % 4

    return


# 일렬로 나열, 4개 이상 연속하면 폭파시키기
def boom():
    temp_list = one_list[:]
    check_again = True
    pop_index = list()
    while check_again:
        # print(temp_list, '==')
        check_again = False
        result_list = list()
        num = 1
        if temp_list:
            prev_num = temp_list[0]
            
            for i in range(1, len(temp_list)):
                if prev_num == temp_list[i]:
                    num += 1
                else:
                    result_list.append([num, prev_num])
                    prev_num = temp_list[i]
                    num = 1
            # 마지막은 수동으로 넣기
            result_list.append([num, prev_num])

            # temp_list 다시 만들기
            temp_list = list()
            for num, prev_num in result_list:
                # print(num, prev_num, '-0-0-')
                if num >= 4:
                    result[prev_num] += num
                    check_again = True
                else:
                    temp_list.extend([prev_num] * num)

        # print(temp_list, '=-=')
        # print(result_list)
    return temp_list


def make_group():
    # 갯수 세어서 하나의 그룹으로 만들기
    result_list = list()
    num = 1
    if one_list:
        prev_num = one_list[0]

        for i in range(1, len(one_list)):
            if prev_num == one_list[i]:
                num += 1
            else:
                # 지금까지 쌓은 갯수 넣기
                result_list.extend([num, prev_num])
                prev_num = one_list[i]
                num = 1

        # 마지막은 수동으로 넣기
        result_list.extend([num, prev_num])

        # print(f"result_list: {result_list}")
    return result_list[:N ** 2]


# 좌 하 우 상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

# 0 상 하 좌 우
ddr = [0, -1, 1, 0, 0]
ddc = [0, 0, 0, -1, 1]

N, M = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0, 0, 0]
ds = list()
for _ in range(M):
    di, si = map(int, input().split())
    ds.append([di, si])

for idx in range(M):
    di, si = ds[idx]
    temp_r = N // 2
    temp_c = N // 2
    # 구슬 파괴
    for _ in range(si):
        temp_r += ddr[di]
        temp_c += ddc[di]
        if 0 <= temp_r < N and 0 <= temp_c < N:
            # result[grounds[temp_r][temp_c]] += 1
            grounds[temp_r][temp_c] = -1

    # print('grounds')
    # for gr in grounds:
    #     print(gr)

    # 순서대로 체크하기, 일렬로 만들기
    one_list = list()
    make_one()
    # print('일렬로 만들기')
    # print(one_list)
    # 4개 이상 연속하는 구슬 폭파
    one_list = boom()
    # print('네 개 이상 폭파')
    # print(one_list)
    # 하나의 그룹으로 만들기
    one_list = make_group()

    # print('하나의 그룹으로')
    # print(one_list)

    # 칸에 순서대로 넣기
    cur_r = N // 2
    cur_c = N // 2
    cur_dir = 0
    num = 1
    idx = 0
    grounds = [[0] * N for _ in range(N)]
    while cur_c >= 0:
        for _ in range(num):
            cur_r += dr[cur_dir]
            cur_c += dc[cur_dir]
            if cur_c == -1:
                break
            if idx < len(one_list):
                # print(f"cur_r: {cur_r}, cur_c: {cur_c}, one_list: {idx, one_list[idx]}")
                grounds[cur_r][cur_c] = one_list[idx]
            else:
                cur_c = -1
                break
            idx += 1
        if cur_dir % 2 == 1:
            num += 1

        cur_dir = (cur_dir + 1) % 4

    # print('result')
    # for gr in grounds:
    #     print(gr)
    # print('==')

# print(result)
ans = 0
for i in range(1, 4):
    ans += result[i] * i
print(ans)

"""
제출하자마자 틀렸습니다
거의 마지막 부분 칸에 순서대로 넣을 때 다음을 추가
if cur_c == -1:
    break

44% 틀렸습니다.
문제 조건대로 풀기,,
4개 이상 폭파시킬 때 
폭파시키고 나서 임의로 첫 번째 idx부터 다시 탐색함
시키는대로 4개 이상 이어지는 부분 다 찾고나서 터뜨린 뒤에
다시 처음부터 탐색해야 한다.
"""
