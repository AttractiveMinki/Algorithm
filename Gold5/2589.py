import sys

sys.stdin = open('test.txt', 'r')

# 2589 보물섬

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, M = map(int, input().split())
rands = [input() for _ in range(N)]
maximum = 0
for r in range(N):
    for c in range(M):
        visited = [[0] * M for _ in range(N)]
        queue = list()
        queue.append([r, c, 0])
        while queue:
            qr, qc, qdis = queue.pop(0)
            if rands[qr][qc] == 'W':
                continue
            visited[qr][qc] = 1
            for i in range(4):
                cr = qr + dr[i]
                cc = qc + dc[i]
                if 0 <= cr < N and 0 <= cc < M and visited[cr][cc] == 0 and rands[cr][cc] == 'L':
                    visited[cr][cc] = 1
                    maximum = max(qdis + 1, maximum)
                    queue.append([cr, cc, qdis + 1])

print(maximum)


### 위는 752ms, 아래는 1208ms. visited 차이. ###

# # 2589 보물섬

# # 상 좌 하 우
# dr = [-1, 0, 1, 0]
# dc = [0, -1, 0, 1]

# N, M = map(int, input().split())
# rands = [input() for _ in range(N)]
# maximum = 0
# for r in range(N):
#     for c in range(M):
#         visited = [[0] * M for _ in range(N)]
#         queue = list()
#         queue.append([r, c, 0])
#         while queue:
#             qr, qc, qdis = queue.pop(0)
#             if visited[qr][qc] == 1 or rands[qr][qc] == 'W':
#                 continue
#             visited[qr][qc] = 1
#             for i in range(4):
#                 cr = qr + dr[i]
#                 cc = qc + dc[i]
#                 if 0 <= cr < N and 0 <= cc < M and visited[cr][cc] == 0 and rands[cr][cc] == 'L':
#                     maximum = max(qdis + 1, maximum)
#                     queue.append([cr, cc, qdis + 1])

# print(maximum)
