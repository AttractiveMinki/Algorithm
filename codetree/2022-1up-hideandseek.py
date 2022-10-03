import sys

sys.stdin = open('./test.txt', 'r')

# 술래잡기

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

n, m, h, k = map(int, input().split())
grounds = [[0] * n for _ in range(n)]
runners = list()
trees = list()

for _ in range(m):
    x, y, d = map(int, input().split())
    if d == 1: # 좌우 움직임, 우 보고 시작
        runners.append([x - 1, y - 1, 3])
    elif d == 2: # 상하 움직임, 아래 보고 시작
        runners.append([x - 1, y - 1, 2])

for _ in range(h):
    x, y = map(int, input().split())
    trees.append([x - 1, y - 1])

# 술래의 움직임을 담은 catcher_position_list를 먼저 만듦
catcher_position_list = [[n // 2, n // 2, 0]]
temp_cnt = 2

while catcher_position_list[-1][0] != 0 or catcher_position_list[-1][1] != 0:
    cur_weight = temp_cnt // 2
    for _ in range(cur_weight):
        cr = catcher_position_list[-1][0]
        cc = catcher_position_list[-1][1]
        cdir = catcher_position_list[-1][2]
        tr = cr + dr[cdir]
        if tr == -1:  # 범위 벗어나면 break
            break
        tc = cc + dc[cdir]
        catcher_position_list.append([tr, tc, cdir])
    # 마지막 위치이동 후 시점 바꿔주기
    catcher_position_list[-1][2] = (catcher_position_list[-1][2] - 1) % 4

    # print(catcher_position_list)
    temp_cnt += 1

# 중앙으로 가기 위해 방향 반대로바꿔주기
temp_catcher_list = catcher_position_list[::-1]
# 0행 0열 2번 있을 필요는 없음
temp_catcher_list.pop(0)

for tr, tc, tdir in temp_catcher_list:
    # temp_catcher와 반대 방향을 봐야 함
    temp_dir = (tdir + 2) % 4
    # 0행 0열이 아니고, 직전 방향과 현재 방향이 다르다면, 직전에 나왔던 틀어지는 시점의 보는 방향 바꿔주기
    if (catcher_position_list[-1][0] != 0 or catcher_position_list[-1][1] != 0) and catcher_position_list[-1][2] != temp_dir:
        catcher_position_list[-1][2] = (catcher_position_list[-1][2] + 1) % 4
    catcher_position_list.append([tr, tc, temp_dir])
# 마지막 위치이동 후 시점 바꿔주기
catcher_position_list[-1][2] = (catcher_position_list[-1][2] + 1) % 4

score = 0
# k턴만큼 반복
catcher_idx = 0
for turn in range(1, k + 1):
    # print(f"before runners: {runners}")
    if runners == []:
        break
    # m명의 도망자가 먼저 움직임
    for _ in range(len(runners)):
        # runners 존재하는 경우에만 체크
        if runners:
            rr, rc, rdir = runners.pop(0)
        else:
            break
        # 거리 3 초과시 continue
        if abs(rr - catcher_position_list[catcher_idx][0]) + abs(rc - catcher_position_list[catcher_idx][1]) > 3:
            runners.append([rr, rc, rdir])
        # 거리 3 이하
        else:
            tr = rr + dr[rdir]
            tc = rc + dc[rdir]
            # 이동 결과가 범위 안에 있다면
            if 0 <= tr < n and 0 <= tc < n:
                # 술래 위치가 아니라면
                if tr != catcher_position_list[catcher_idx][0] or tc != catcher_position_list[catcher_idx][1]:
                    runners.append([tr, tc, rdir])
                else:
                    runners.append([rr, rc, rdir])
            else:
                rdir = (rdir + 2) % 4 # rdir 반대로 설정
                tr = rr + dr[rdir]
                tc = rc + dc[rdir]
                # 술래가 그 위치에 없다면 이동
                if tr != catcher_position_list[catcher_idx][0] or tc != catcher_position_list[catcher_idx][1]:
                    runners.append([tr, tc, rdir])
                # 술래가 그 위치에 있다면 제자리
                else:
                    runners.append([rr, rc, rdir])
    # print(f"after runners: {runners}")

    # 술래가 움직임
    catcher_idx = (catcher_idx + 1) % len(catcher_position_list)
    cr, cc, cdir = catcher_position_list[catcher_idx]
    # print(f"current catcher position cr: {cr}, cc: {cc}, cdir: {cdir}")
    # 시야 안에 있는 도망자를 잡는다.
    if 0 <= cr < n and 0 <= cc < n:
        # 나무가 있다면 continue
        have_tree = False
        for tree_r, tree_c in trees:
            if cr == tree_r and cc == tree_c:
                have_tree = True
                break
        # 나무가 없다면
        if have_tree == False:
            temp_runners = list()
            for runner_r, runner_c, runner_dir in runners:
                # 잡음
                if runner_r == cr and runner_c == cc:
                    score += turn
                # 못잡음
                else:
                    temp_runners.append([runner_r, runner_c, runner_dir])
            runners = temp_runners[:]
    # 2칸 더 반복
    for _ in range(2):
        cr = cr + dr[cdir]
        cc = cc + dc[cdir]
        if 0 <= cr < n and 0 <= cc < n:
            # 나무가 있다면 continue
            have_tree = False
            for tree_r, tree_c in trees:
                if cr == tree_r and cc == tree_c:
                    have_tree = True
                    break
            # 나무가 없다면
            if have_tree == False:
                temp_runners = list()
                for runner_r, runner_c, runner_dir in runners:
                    # 잡음
                    if runner_r == cr and runner_c == cc:
                        score += turn
                    # 못잡음
                    else:
                        temp_runners.append([runner_r, runner_c, runner_dir])
                runners = temp_runners[:]
    # print(f"runners: {runners}, turn: {turn}, score: {score}")

print(score)

"""
20% 틀렸습니다. (test case 4번)
술래가 자기 자리 포함 세 칸에서 runners가 있는지를 체크해야 함.
제자리에서 tree가 있는지 여부를 확인하지 않음

런타임 에러
runners가 없을 때를 고려하지 않음

33% 틀렸습니다. (test case 6번)
# 이동 결과가 범위 안에 있으면서 술래 위치가 아니라면
부분 로직 다소 수정 (문제 조건대로 수정)
+
for _ in range(m)을
fur _ in range(len(runners))로 변경
"""
