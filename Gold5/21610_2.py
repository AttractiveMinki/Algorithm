import sys

sys.stdin = open('BJ/test.txt', 'r')

# 21610 마법사 상어와 비바라기

# 0 좌 좌상 상 우상 우 우하 하 좌하
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 좌상 좌하 우하 우상
ddr = [-1, 1, 1, -1]
ddc = [-1, -1, 1, 1]

N, M = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]
move_info = [list(map(int, input().split())) for _ in range(M)]
clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
# for gr in grounds:
#     print(gr)
# print('---')
# for info in move_info:
#     print(info)
# print('clouds')
# for cl in clouds:
#     print(cl)
# print('###')

for idx in range(M):
    # 1. 모든 구름이 di방향으로 si칸 이동한다.
    di, si = move_info[idx]
    si = si % N
    for cl_idx in range(len(clouds)):
        cl_r = clouds[cl_idx][0]
        cl_c = clouds[cl_idx][1]
        cl_r = (cl_r + dr[di] * si) % N
        cl_c = (cl_c + dc[di] * si) % N
        clouds[cl_idx][0] = cl_r
        clouds[cl_idx][1] = cl_c

    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    visited = [[0] * N for _ in range(N)]
    for cl_r, cl_c in clouds:
        grounds[cl_r][cl_c] += 1
        visited[cl_r][cl_c] = 1

    # 3. 구름이 모두 사라진다.

    # 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 사용한다.
    for cl_r, cl_c in clouds:
        cnt = 0
        for i in range(4):
            cr = cl_r + ddr[i]
            cc = cl_c + ddc[i]
            if 0 <= cr < N and 0 <= cc < N and grounds[cr][cc] > 0:
                cnt += 1
        grounds[cl_r][cl_c] += cnt

    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물 양이 2 줄어든다. 구름이 생기는 칸은 3에 없는 칸이어야 함.
    temp_clouds = list()
    for r in range(N):
        for c in range(N):
            if grounds[r][c] >= 2 and visited[r][c] == 0:
                temp_clouds.append([r, c])
                grounds[r][c] -= 2
    clouds = temp_clouds[:]

    # print(f"{idx + 1}번째 결과")
    # for gr in grounds:
    #     print(gr)
    # print(f"cloud 현황")
    # for cl in clouds:
    #     print(cl)

result = 0
for r in range(N):
    result += sum(grounds[r])

print(result)

"""
- 1번 예제 답 72인가 나옴
2번 안에서 4번을 처리해주려다가 참사 발생

- 시간 초과
5번에서 if grounds[r][c] >= 2 and [r, c] not in clouds: 사용
자체 계산 결과
M 100
r, c 2500
clouds 2500
시간복잡도 2500만 * 25

[r, c] not in clouds 대신에,
위에서 만든 visited를 체크하는 것으로 대체함.

"""
