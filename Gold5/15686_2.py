import sys

sys.stdin = open('test.txt', 'r')

# 15686 치킨 배달

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# 치킨 최솟값 갱신
def check(temp_list):
    visited = [[0] * N for _ in range(N)]
    queue = list()
    for i in temp_list:
        temp_r, temp_c = chicken[i]
        visited[temp_r][temp_c] = 1
        queue.append([temp_r, temp_c])
    while queue:
        cr, cc = queue.pop(0)
        for i in range(4):
            tr = cr + dr[i]
            tc = cc + dc[i]
            if 0 <= tr < N and 0 <= tc < N and visited[tr][tc] == 0:
                visited[tr][tc] = visited[cr][cc] + 1
                queue.append([tr, tc])

    result = 0
    # 집에서 가장 먼 곳의 거리 측정하고 1 빼줌
    for hr, hc in home:
        result += (visited[hr][hc] - 1)
    answer[0] = min(result, answer[0])
    return

# nCr 구현
def comb(level):
    if level == M:
        check(temp_list)
        return
    for i in range(level, len(chicken)):
        if temp_list == [] or temp_list[-1] < i:
            temp_list.append(i)
            comb(level + 1)
            temp_list.pop()

N, M = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]
home = list()
chicken = list()
for r in range(N):
    for c in range(N):
        # 가정집인 곳 고르기
        if grounds[r][c] == 1:
            home.append([r, c])
        # 치킨집인 곳 고르기
        elif grounds[r][c] == 2:
            chicken.append([r, c])

answer = [987654321]
temp_list = list()
comb(0)
print(answer[0])


### 주석 포함 ###
# import sys

# sys.stdin = open('test.txt', 'r')

# # 15686 치킨 배달

# # 상 좌 하 우
# dr = [-1, 0, 1, 0]
# dc = [0, -1, 0, 1]

# # 치킨 최솟값 갱신
# def check(temp_list):
#     visited = [[0] * N for _ in range(N)]
#     queue = list()
#     # print(f'temp_list: {temp_list}')
#     for i in temp_list:
#         temp_r, temp_c = chicken[i]
#         visited[temp_r][temp_c] = 1
#         queue.append([temp_r, temp_c])
#     # print(f"queue: {queue}")
#     while queue:
#         cr, cc = queue.pop(0)
#         for i in range(4):
#             tr = cr + dr[i]
#             tc = cc + dc[i]
#             if 0 <= tr < N and 0 <= tc < N and visited[tr][tc] == 0:
#                 visited[tr][tc] = visited[cr][cc] + 1
#                 queue.append([tr, tc])

#     # temp_maximum = 0
#     result = 0
#     # 집에서 가장 먼 곳의 거리 측정하고 1 빼줌
#     for hr, hc in home:
#         # temp_maximum = max(visited[hr][hc], temp_maximum)
#         # print(f"visited[hr][hc]: {visited[hr][hc]}, maximum: {temp_maximum}")
#         result += (visited[hr][hc] - 1)
#     # minimum[0] = min(temp_maximum - 1, minimum[0])
#     # print(f"minimum: {minimum[0]}")
#     # print(f"result: {result}, answer: {answer[0]}")
#     answer[0] = min(result, answer[0])
#     return

# # nCr 구현
# def comb(level):
#     if level == M:
#         check(temp_list)
#         return
#     for i in range(level, len(chicken)):
#         if temp_list == [] or temp_list[-1] < i:
#             temp_list.append(i)
#             comb(level + 1)
#             temp_list.pop()

# N, M = map(int, input().split())
# grounds = [list(map(int, input().split())) for _ in range(N)]
# home = list()
# chicken = list()
# for r in range(N):
#     for c in range(N):
#         # 가정집인 곳 고르기
#         if grounds[r][c] == 1:
#             home.append([r, c])
#         # 치킨집인 곳 고르기
#         elif grounds[r][c] == 2:
#             chicken.append([r, c])

# # minimum = [N * N]
# answer = [987654321]
# temp_list = list()
# comb(0)
# # print(minimum[0])
# print(answer[0])
