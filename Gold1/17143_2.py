import sys

sys.stdin = open('BJ/test.txt', 'r')

# 17143 낚시왕 - pypy 정답, python 3 20% 시간초과

# 0, 상, 하, 우, 좌
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]

R, C, M = map(int, input().split())
sharks = [[[] for _ in range(C + 1)] for _ in range(R + 1)]

# for sh in sharks:
#     print(sh)

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[r][c].append([s, d, z]) # 속력, 이동방향, 크기

# print('---')
# for sh in sharks:
#     print(sh)

answer = 0
# 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
for fisher_c in range(1, C + 1):
    # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
    for temp_r in range(1, R + 1):
        if sharks[temp_r][fisher_c]:
            _, _, cur_z = sharks[temp_r][fisher_c].pop()
            answer += cur_z
            print(f"{temp_r}, {fisher_c} 좌표의 무게 {cur_z}를 잡음")
            print(f"answer: {answer}")
            break

    # 3. 상어가 이동한다.
    temp_sharks = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if sharks[r][c]:
                cr = r
                cc = c
                # print(sharks[r][c])
                # 속력, 이동방향, 크기
                cur_s, cur_d, cur_z = sharks[r][c][0]

                # 상하
                if cur_d <= 2:
                    temp_cur_s = cur_s % ((R - 1) * 2)
                    # print(f"cr: {cr}, cc: {cc}, temp_cur_s: {temp_cur_s}, cur_s: {cur_s}, R: {R}")
                # 좌우
                else:
                    temp_cur_s = cur_s % ((C - 1) * 2)
                    # print(f"cr: {cr}, cc: {cc}, temp_cur_s: {temp_cur_s}, cur_s: {cur_s}, C: {C}")

                # 갈 칸 정하기
                # 속력만큼 이동
                for _ in range(temp_cur_s):
                    cr = cr + dr[cur_d]
                    cc = cc + dc[cur_d]
                    # 범위 안에 있으면 continue
                    if 0 < cr <= R and 0 < cc <= C:
                        continue
                    # 범위 안에 있지 않다면 상 -> 하, 좌 -> 우
                    if cur_d % 2 == 0:
                        cur_d -= 1
                    else:
                        cur_d += 1
                    # 반대 방향으로 이동
                    cr = cr + dr[cur_d] * 2
                    cc = cc + dc[cur_d] * 2

                # 비어있다면 temp_sharks에 넣기
                if not temp_sharks[cr][cc]:
                    temp_sharks[cr][cc].append([cur_s, cur_d, cur_z])
                else:
                    # 기존 것이 크다면 continue
                    print(temp_sharks[cr][cc][0], cur_z)
                    if temp_sharks[cr][cc][0][-1] > cur_z:
                        continue
                    else:
                        temp_sharks[cr][cc][0] = [cur_s, cur_d, cur_z]
    sharks = [te[:] for te in temp_sharks]
    #
    # print('temp_sharks')
    # for sh in sharks:
    #     print(sh)
    # print(f"answer: {answer}")

print(answer)

"""
## TypeError ##
삼중리스트 관련 에러가 있었던 것 같음

수정 전
temp_sharks[cr][cc] = [cur_s, cur_d, cur_z]
수정 후
temp_sharks[cr][cc][0] = [cur_s, cur_d, cur_z]


## 16% 시간초과 ##
한 칸 한 칸 봐서 시간이 오래 걸린 듯.
중복된 연산은 하지 않도록 알고리즘 수정

# 상하
if cur_d <= 2:
    temp_cur_s = cur_s % (R * 2)
# 좌우
else:
    temp_cur_s = cur_s % (C * 2)
    
## 제출하자마자 틀렸습니다 ##
계산해보니 R, C 대신 R - 1, C - 1을 사용해야 함.

수정 전
temp_cur_s = cur_s % (R * 2)
temp_cur_s = cur_s % (C * 2)

수정 후
temp_cur_s = cur_s % ((R - 1) * 2)
temp_cur_s = cur_s % ((C - 1) * 2)
"""
