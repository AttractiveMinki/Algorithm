import sys

sys.stdin = open('test.txt', 'r')

# 2660 회장 뽑기

N = int(input())
friends = [[] for _ in range(N + 1)]
while True:
    num1, num2 = map(int, input().split())
    if num1 == -1:
        break
    friends[num1].append(num2)
    friends[num2].append(num1)

minimum_score = 100
ceo = list()
for i in range(1, N + 1):
    visited = [0] * (N + 1)

    queue = list()
    for fr in friends[i]:
        queue.append([fr, 0])
    while queue:
        cur_friend, cur_score = queue.pop(0)
        if visited[cur_friend] != 0:
            continue
        visited[cur_friend] = cur_score + 1
        for num in friends[cur_friend]:
            # 자기 자신은 방문하지 않는다.
            if num == i:
                continue
            if visited[num] == 0:
                queue.append([num, cur_score + 1])
    
    cur_per_score = max(visited)
    # print(i, visited)
    # print(cur_per_score, minimum_score)
    if cur_per_score < minimum_score:
        minimum_score = cur_per_score
        ceo = [i]
    elif cur_per_score == minimum_score:
        ceo.append(i)

print(minimum_score, len(ceo))
print(' '.join(map(str, ceo)))

# 45% 틀림
# visited == 1인 경우만 체크해서 틀린 듯.
# visited != 0인 경우로 수정

# 63% 반례 - 자기 자신을 방문하는 경우는 계산에서 제외해야 한다.
# 1번 방문시, visited[1] != 0인 문제가 발생 -> if num == i 추가
"""
5
1 2
1 3
1 4
1 5
-1 -1
"""
