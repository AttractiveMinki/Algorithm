import sys

sys.stdin = open('test.txt', 'r')

# 9205 맥주 마시면서 걸어가기

# import sys

# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    home_r, home_c = list(map(int, input().split()))
    conven = list()
    for _ in range(N):
        temp_r, temp_c = list(map(int, input().split()))
        conven.append([temp_r, temp_c])
    final_r, final_c = list(map(int, input().split()))
    conven.append([final_r, final_c])
    queue = list()
    queue.append([home_r, home_c])

    answer = 'sad'
    visited = [0] * len(conven)
    while queue:
        cur_r, cur_c = queue.pop()
        for idx, (con_r, con_c) in enumerate(conven):
            cur_dis = abs(con_r - cur_r) + abs(con_c - cur_c)
            if cur_dis <= 1000 and visited[idx] == 0:
                visited[idx] = 1
                queue.append([con_r, con_c])
                if con_r == final_r and con_c == final_c:
                    answer = 'happy'
                    break

    print(answer)
