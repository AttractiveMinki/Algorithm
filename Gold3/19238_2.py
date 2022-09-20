import sys

sys.stdin = open('BJ/test.txt', 'r')

# 19238 스타트 택시

# 택시의 움직임을 나타냄, 움직인 거리가 return
def move(current_cus_r, current_cus_c, end_pos_r, end_pos_c):
    temp_visited_2 = [vi[:] for vi in visited]
    temp_visited_2[current_cus_r][current_cus_c] = 1
    queue =[[current_cus_r, current_cus_c, 0]] # r, c, distance 담김
    while queue:
        qr, qc, qdis = queue.pop(0)
        for i in range(4):
            cr = qr + dr[i]
            cc = qc + dc[i]
            # 범위 안에 있으면서 방문한 적이 없다면
            if 0 < cr <= N and 0 < cc <= N and temp_visited_2[cr][cc] == 0:
                temp_visited_2[cr][cc] = 1
                # 목적지에 도달했다면 거리 계산해서 return
                if cr == end_pos_r and cc == end_pos_c:
                    return qdis + 1
                queue.append([cr, cc, qdis + 1])
    # 목적지에 도달하지 못하고 queue 빠져나왔다면 -1 return
    return -1


# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, M, fuel = map(int, input().split())
grounds = [[1] * (N + 1)] + [[1] + list(map(int, input().split())) for _ in range(N)]
visited = [[0] * (N + 1) for _ in range(N + 1)]
for r in range(N + 1):
    for c in range(N + 1):
        if grounds[r][c] == 1:
            visited[r][c] = 1

start_r, start_c = map(int, input().split())
customer = list()
for _ in range(M):
    cus_r, cus_c, end_r, end_c = map(int, input().split())
    customer.append([cus_r, cus_c, end_r, end_c])

while customer:
    # 택시 위치 정하기
    queue = [[start_r, start_c]]
    # 임시 방문 목록, 임시 grounds 만들기
    temp_visited = [vi[:] for vi in visited]
    temp_visited[start_r][start_c] = 1 # 현재 택시 위치 방문 표시
    temp_grounds = [gr[:] for gr in grounds]
    while queue:
        qr, qc = queue.pop(0)
        for i in range(4):
            cr = qr + dr[i]
            cc = qc + dc[i]
            # 범위 안에 있으면서 방문한 적이 없는 경우
            if 0 < cr <= N and 0 < cc <= N and temp_visited[cr][cc] == 0:
                temp_visited[cr][cc] = 1
                temp_grounds[cr][cc] = temp_grounds[qr][qc] + 1
                queue.append([cr, cc])

    # 승객 중 최소 거리 구하기
    cus_idx = -1
    cus_minimum = 98765
    end_pos_r = start_r
    end_pos_c = start_c

    for idx, (current_r, current_c, current_end_r, current_end_c) in enumerate(customer):
        # 택시 출발지와 손님 출발지가 같을 경우 바로 return
        if current_r == start_r and current_c == start_c:
            # customer 내 idx, customer 최소 이동거리, 손님 시작 지점 r c, 손님 목적지 r c 갱신
            cus_idx = idx
            cus_minimum = temp_grounds[current_r][current_c]
            current_cus_r = current_r
            current_cus_c = current_c
            end_pos_r = current_end_r
            end_pos_c = current_end_c
            break
        # grounds가 유효한 값이면서 현재 최소거리보다 더 작은 거리인 경우
        if temp_grounds[current_r][current_c] > 0 and cus_minimum > temp_grounds[current_r][current_c]:
            cus_idx = idx
            cus_minimum = temp_grounds[current_r][current_c]
            current_cus_r = current_r
            current_cus_c = current_c
            end_pos_r = current_end_r
            end_pos_c = current_end_c
        # grounds가 유효한 값이면서 현재 최소거리와 같은 경우
        elif temp_grounds[current_r][current_c] > 0 and cus_minimum == temp_grounds[current_r][current_c]:
            # 행이 더 작은 경우 갱신
            if current_cus_r > current_r:
                cus_idx = idx
                cus_minimum = temp_grounds[current_r][current_c]
                current_cus_r = current_r
                current_cus_c = current_c
                end_pos_r = current_end_r
                end_pos_c = current_end_c
            # 행은 같지만 열이 더 작은 경우 갱신
            elif current_cus_r == current_r and current_cus_c > current_c:
                cus_idx = idx
                cus_minimum = temp_grounds[current_r][current_c]
                current_cus_r = current_r
                current_cus_c = current_c
                end_pos_r = current_end_r
                end_pos_c = current_end_c

    # cus_idx가 없으면 break
    if cus_idx == -1:
        fuel = -1
        break
    # 현재 보고 있는 customer의 정보 방출
    customer.pop(cus_idx)

    # 연료 빼주기
    fuel -= cus_minimum
    if fuel < 0:
        fuel = -1
        break

    # 승객 위치로 이동
    move_dis = move(current_cus_r, current_cus_c, end_pos_r, end_pos_c)
    # 사용한 연료 계산
    fuel -= move_dis
    # 연료가 0보다 작거나 move_dis == -1인 경우(유효한 움직임이 아님)
    if fuel < 0 or move_dis == -1:
        fuel = -1
        break
    # 2배 충전
    fuel += (move_dis * 2)

    # 택시 시작 위치 재설정
    start_r = end_pos_r
    start_c = end_pos_c

print(fuel)

"""
0% 틀렸습니다.
cus_idx == -1일 때 예외처리 추가
택시 출발지와 손님 출발지 같을 경우 고려

80% 틀렸습니다.
move 함수의 결과인 move_dis가 move_dis == -1 일 때 예외처리 추가

### 참고) 손님 위치의 행(r), 열(c) 계산시
delta 탐색 순서를 상 좌 하 우 로 했다고 해서 안심할 수 없고, 택시와의 거리가 최솟값인 손님들 일일이 행, 열 보고 판단해야 함.

ㅂ=빈칸
ㅃ=손님
ㅇ=택시

ㅂㅂㅂㅂㅂㅃ
ㅃㅂㅂㅇㅂㅂ
ㅂㅂㅂㅂㅂㅂ

위의 예시에서, 1행 6열 손님을 태워야 하지만
상 좌 하 우 순서로 탐색하면, 2행 1열 손님을 태우는 것으로 인지하게 됨. 
따라서 거리 최솟값이 같은 손님이라면 일일이 대조해봐야 됨.
"""