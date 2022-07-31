import sys

sys.stdin = open('test.txt', 'r')

# 16508 전공책

words = input()
N = int(input())
cost = list()
title = list()
for _ in range(N):
    co, ti = input().split()
    cost.append(co)
    title.append(ti)

minimum = 1e9

for i in range(2 ** N):
    num = bin(i)[2:].zfill(N)
    temp_min = 0
    visited = [0] * len(words)
    for idx, nu in enumerate(num):
        # 탐색할 책이라면
        if nu == "1":
            temp_min += int(cost[idx])
            # backtracking
            if temp_min > minimum:
                continue
            title_visited = [0] * len(title[idx])
            # 주어진 title 전체탐색
            for ti_idx, ti in enumerate(title[idx]):
                # 주어진 ANT 전체탐색
                for word_idx in range(len(words)):
                    # 방문한 곳이면 continue
                    if visited[word_idx] == 1 or title_visited[ti_idx] == 1:
                        continue
                    # title과 현재 단어가 같다면 방문처리
                    if words[word_idx] == ti:
                        visited[word_idx] = 1
                        title_visited[ti_idx] = 1
    
    if sum(visited) == len(words):
        minimum = min(temp_min, minimum)
if minimum == 1e9:
    minimum = -1
print(minimum)
