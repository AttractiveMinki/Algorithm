import sys

sys.stdin = open('test.txt', 'r')

# 17142 연구소 3

# 상 좌 하 우
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

# virus index가 골라졌을 때 최소 길이 구하기
def calc(virus_indexes):
    # 방문 처리 겸 길이 계산하는 리스트
    visited = [[0] * N for _ in range(N)]
    # 큐로 탐색
    queue = list()
    # 선택한 바이러스 인덱스
    for index in virus_indexes:
        ir, ic = virus[index]
        # 지금 선택한 바이러스 방문처리 및 큐에 넣기
        visited[ir][ic] = 1
        queue.append([ir, ic])

    while queue:
        qr, qc = queue.pop(0)
        for i in range(4):
            cr = qr + dr[i]
            cc = qc + dc[i]
            # 방문하지 않았으면서 벽이 아닌 곳
            if 0 <= cr < N and 0 <= cc < N and visited[cr][cc] == 0 and grounds[cr][cc] != 1:
                visited[cr][cc] = visited[qr][qc] + 1
                queue.append([cr, cc])

    # 결과 리턴을 위한 계산
    result = 0
    for r in range(N):
        for c in range(N):
            # 비활성화 바이러스일 경우도 생각하기
            if grounds[r][c] == 2:
                visited[r][c] = 1
            # 땅인데 방문한 곳이 없다 -> 계산하면 안 됨 -> 그냥 return
            if grounds[r][c] == 0 and visited[r][c] == 0:
                return
            # result 최댓값으로 갱신
            result = max(visited[r][c], result)

    # 시작점의 visited가 1이었으니 도착점의 visited도 1 빼줌
    result -= 1
    # print(f"result: {result}, minimum: {minimum[0]}")
    # minimum값 갱신
    minimum[0] = min(result, minimum[0])
    return
    

# 재귀로 combination 구현
def recur(level, start):
    if level == M:
        # print(virus_indexes)
        calc(virus_indexes)
        return
    
    # virus index로 combination 구함. nCr 에서 n = len(virus), c = M
    for i in range(start, len(virus)):
        virus_indexes.append(i)
        recur(level + 1, i + 1) # i + 1자리에 start + 1 넣었다가 고생함
        virus_indexes.pop()

N, M = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]

# 바이러스 위치 저장
virus = list()
for r in range(N):
    for c in range(N):
        if grounds[r][c] == 2:
            virus.append([r, c])

# 최솟값 저장
minimum = [N * N + 1]
# 바이러스 index 데리고 다닐 리스트 선언
virus_indexes = list()
recur(0, 0)
# minimum 갱신 안됐으면 -1로
if minimum[0] == N * N + 1:
    minimum[0] = -1
print(minimum[0])

"""
제출하자마자 틀렸습니다.
모든 칸에 바이러스를 퍼뜨릴 수 없는 경우의 수를 생각하지 않음.


72% 틀렸습니다.
grounds[r][c] == 0 and visited[r][c] == 0일 때 minimum[0] = -1로 박고 return 및
recur에서 if minimum[0] == -1: return으로 백트래킹함.

5 2
0 0 1 0 0
0 0 1 2 0
0 0 1 1 1
0 2 0 0 0
2 0 0 0 0
이런 상황에서 왼쪽 아래 두 개가 걸리면 바로 백트래킹 -> 원인이라 생각
    (오른쪽 위 2와 왼쪽 아래 2를 골랐을 때 답이 나올 수 있는데, 답이 없다고 처리했기 때문)
minimum[0] = -1과 백트래킹 때려치고 return만 함.


92% 틀렸습니다.
예제 7에서 틀림,,, 예제 7개나 있는지도몰랐네
안돌려보고 제출한거쥬,,,,,
5 1
2 2 2 1 1
2 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 1 1

grounds[r][c] == 2일 때 continue했었는데
모두 다 2일 때 답이 -1로 나오는 현상이 있었음.
"""