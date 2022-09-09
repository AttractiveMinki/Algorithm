import sys

sys.stdin = open('test.txt', 'r')

# 15685 드래곤 커브

# 우 상 좌 하
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

N = int(input())
visited = [[0] * 101 for _ in range(101)]

numbers = list()
for _ in range(N):
    x, y, d, g = map(int, input().split())
    numbers.append([x, y, d, g])
    # 초기화, g=0일 때 미리 설정
    visited[y][x] = 1
    x += dx[d]
    y += dy[d]
    d += 1
    d %= 4
    visited[y][x] = 1
    stack = [[x, y, d]]
    
    for i in range(g):
        temp_stack = stack[:]
        while stack:
            sx, sy, sd = stack.pop()
            x += dx[sd]
            y += dy[sd]
            td = (sd + 1) % 4
            temp_stack.append([x, y, td])
            visited[y][x] = 1
        stack = temp_stack[:]

cnt = 0
for r in range(0, 100):
    for c in range(0, 100):
        if visited[r][c] == 1 and visited[r][c + 1] == 1 and visited[r + 1][c] == 1 and visited[r + 1][c + 1] == 1:
            cnt += 1

print(cnt)

"""
평소 r, c로 풀었기 때문에 y, x꼴로 푸는 건 살짝 어색했지만, 그대로 진행

x, y 설정과 g 설정은 어렵지 않았음
세대를 거침에 따라 d, 방향이 바뀌는 것이 핵심이었음.
어떻게 구현할까? -> stack처럼 선입선출을 이용해, stack의 제일 마지막으로 이동한 방향에서 시계 방향으로 90도
이동하는 꼴을 구현함. dr += 1, dr %= 4로 구현함.
visited를 찍어보니 처음엔 이상한 결과가 나옴

1. 
g=0일 때 값을 미리 설정하지 않으면, stack에 짝수 개의 입력이 들어감을 확인.
g=1일 때, _ㅣ- 꼴이 나옴. _ㅣ꼴을 원하는 문제와 다름.
초기값 _을 설정해주고, 이후 g를 반복할 때 ㅣ를 만들어주도록 코드 설정.

2. 
stack의 sx, sx를 참고하여 stack에 넣을 x, y를 만드는 꼴에서 잘못됨을 느낌
점을 찍는 위치 x, y는 stack에 들어간 좌표가 아니라, 현재 참조하고 있는 x, y를 기준으로 정해야 함.
tx, ty를 구하는 꼴에서, x, y를 그대로 사용하는 꼴로 변경


예전에 정말 고생하면서 풀었던 기억이 나서 풀기 싫었는데, 풀면서 생각보다 스무스하게 진행됨.
한 번 풀었던 문제라서 그런지는 잘 모르겠음. 아무튼 기분은 좋다.
처음 문제를 풀 당시에 stack을 사용하여 꼬리를 무는 개념과, delta[dr, dc]를 사용할 생각을 하지 못해 많은 시간이 소요되었던 것 같음.
위 아이디어를 살짝 알고 있는 상태에서 문제를 풀어서 상대적으로 적은 시간이 소요된 것 같다.
"""
