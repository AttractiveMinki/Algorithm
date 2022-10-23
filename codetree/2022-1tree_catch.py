import sys

sys.stdin = open('./test.txt', 'r')

# 2022-1 나무박멸

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

## 좌상 좌하 우하 우상
ddr = [-1, 1, 1, -1]
ddc = [-1, -1, 1, 1]

N, M, K, C = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]
fire = [[0] * N for _ in range(N)]
result = 0

for idx in range(1, M + 1):
    # 1. 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다.
    temp_grounds = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if grounds[r][c] > 0:
                cnt = 0
                for i in range(4):
                    cr = r + dr[i]
                    cc = c + dc[i]
                    if 0 <= cr < N and 0 <= cc < N and grounds[cr][cc] > 0:
                        cnt += 1
                temp_grounds[r][c] += cnt

    for r in range(N):
        for c in range(N):
            grounds[r][c] += temp_grounds[r][c]

    # 2, 기존에 있었던 나무들은 인접 4칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식 진행
    temp_grounds = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if grounds[r][c] > 0:
                cnt = 0
                for i in range(4):
                    cr = r + dr[i]
                    cc = c + dc[i]
                    if 0 <= cr < N and 0 <= cc < N and grounds[cr][cc] == 0 and fire[cr][cc] == 0:
                        cnt += 1
                if cnt == 0:
                    continue
                tree_num = grounds[r][c] // cnt

                for i in range(4):
                    cr = r + dr[i]
                    cc = c + dc[i]
                    if 0 <= cr < N and 0 <= cc < N and grounds[cr][cc] == 0 and fire[cr][cc] == 0:
                        temp_grounds[cr][cc] += tree_num

    for r in range(N):
        for c in range(N):
            grounds[r][c] += temp_grounds[r][c]

    # 3. 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
    # 중복시 행, 열 작은 순
    temp_grounds = [[0] * N for _ in range(N)]
    temp_r = 0
    temp_c = 0
    temp_max = 0
    for r in range(N):
        for c in range(N):
            # 대각선 네 방향
            if grounds[r][c] > 0:
                temp_grounds[r][c] += grounds[r][c]
                for i in range(4):
                    # K만큼 반복 이동
                    cr = r
                    cc = c
                    for _ in range(K):
                        cr = cr + ddr[i]
                        cc = cc + ddc[i]
                        if 0 <= cr < N and 0 <= cc < N:
                            if grounds[cr][cc] > 0:
                                temp_grounds[r][c] += grounds[cr][cc]
                            # 나무 뒤는 더 이상 보지 않음
                            else:
                                break
                        # 칸을 벗어나거나 제초제가 있다면 break
                        # else:
                        #     break

                if temp_grounds[r][c] > temp_max:
                    temp_max = temp_grounds[r][c]
                    temp_r = r
                    temp_c = c

    # 결과 계산
    result += temp_max

    # 제초제 뿌리기
    fire[temp_r][temp_c] = idx
    grounds[temp_r][temp_c] = 0
    for i in range(4):
        cr = temp_r
        cc = temp_c
        for _ in range(K):
            cr = cr + ddr[i]
            cc = cc + ddc[i]
            if 0 <= cr < N and 0 <= cc < N:
                fire[cr][cc] = idx
                # 나무가 없거나 성이면 그 칸까지 제초제 뿌린다.
                if grounds[cr][cc] <= 0:
                    break
                grounds[cr][cc] = 0

    # 제초제가 c + 1년째 되면 사라진다.
    for r in range(N):
        for c in range(N):
            if fire[r][c] > 0 and fire[r][c] + C <= idx:
                fire[r][c] = 0

print(result)

"""
tc 5번 틀렸습니다.
5 4 1 3 
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 -1 -1 -1
16 0 -1 16 -1

내 답: 47
정답: 48
temp_r, temp_c, temp_max -1으로 초기화
->
temp_r, temp_c, temp_max 0으로 초기화


tc 7번 틀렸습니다.

11 446 20 3
0 0 0 -1 57 0 -1 0 0 0 0 
0 18 0 -1 -1 0 0 0 0 0 45 
64 0 10 0 0 -1 74 0 0 33 0 
0 61 0 0 -1 0 0 0 0 0 -1 
0 66 0 0 0 0 0 0 16 0 0 
7 0 0 0 6 0 0 -1 27 72 0 
0 0 0 0 0 54 0 42 -1 -1 0 
0 0 -1 0 0 0 0 1 0 0 98 
-1 98 68 0 0 75 1 93 0 0 0 
0 0 0 0 77 0 0 -1 0 0 0 
0 -1 0 -1 0 0 0 0 45 0 0 

내 답: 17754
정답: 663822


fire 조건을 체크하지 않도록 수정.
혹은 if문 아래에 else: break 달아도 된다.

수정 이전
if 0 <= cr < N and 0 <= cc < N and fire[cr][cc] == 0:
    if grounds[cr][cc] > 0:
        temp_grounds[r][c] += grounds[cr][cc]
    # 나무 뒤는 더 이상 보지 않음
    else:
        break
        
수정 이후
if 0 <= cr < N and 0 <= cc < N:
    if grounds[cr][cc] > 0:
        temp_grounds[r][c] += grounds[cr][cc]
    # 나무 뒤는 더 이상 보지 않음
    else:
        break

혹은

if 0 <= cr < N and 0 <= cc < N and fire[cr][cc] == 0:
    if grounds[cr][cc] > 0:
        temp_grounds[r][c] += grounds[cr][cc]
    # 나무 뒤는 더 이상 보지 않음
    else:
        break
else:
    break
    
5 4 3 4
5 0 0 0 4
0 0 0 0 -1
0 0 0 -1 0
0 0 0 0 0
5 1 0 0 0

49 나와야 함
"""