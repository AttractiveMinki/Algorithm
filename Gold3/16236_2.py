import sys

sys.stdin = open('BJ/test.txt', 'r')

# 16236 아기 상어

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N = int(input())
grounds = [list(map(int, input().split())) for _ in range(N)]
shark_r = -1
shark_c = -1
shark_size = 2
shark_eat = 0
for r in range(N):
    for c in range(N):
        if grounds[r][c] == 9:
            shark_r = r
            shark_c = c

result = 0
while True:
    fishes = list()
    # 물고기 체크
    queue = [[shark_r, shark_c, 0]]
    visited = [[0] * N for _ in range(N)]
    visited[shark_r][shark_c] = 1
    while queue:
        qr, qc, qdis = queue.pop(0)
        for i in range(4):
            cr = qr + dr[i]
            cc = qc + dc[i]
            if 0 <= cr < N and 0 <= cc < N and visited[cr][cc] == 0 and grounds[cr][cc] <= shark_size:
                visited[cr][cc] = 1
                queue.append([cr, cc, qdis + 1])
                if 0 < grounds[cr][cc] < shark_size:
                    fishes.append([qdis + 1, cr, cc])

    # for fish in fishes:
    #     print(fish)
    # print('--')

    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 엄마 상어에게 도움 요청
    if fishes == []:
        break

    # 거리가 가장 가까운 물고기를 먹으러 간다.
    fishes.sort()
    cur_distance, cur_r, cur_c = fishes.pop(0)
    # print(f"cur_distance: {cur_distance}, cur_r: {cur_r}, cur_c: {cur_c}")

    # 현재 위치 초기화
    grounds[shark_r][shark_c] = 0

    # 먹은 위치로 이동
    grounds[cur_r][cur_c] = 9

    # 현재 위치 갱신
    shark_r = cur_r
    shark_c = cur_c

    # 이동거리 체크
    result += cur_distance

    # 크기만큼 먹으면 크기 1 증가
    shark_eat += 1
    if shark_size == shark_eat:
        shark_size += 1
        shark_eat = 0

# for gr in grounds:
#     print(gr)
# print('--')

print(result)
