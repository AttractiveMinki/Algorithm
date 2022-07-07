import sys

sys.stdin = open('test.txt', 'r')

# 1497 기타 콘서트

N, M = map(int, input().split())
guitars = list()

# 기타 입력받기
for _ in range(N):
    _, guitar = input().split()
    guitars.append(guitar)

# 최대 기타 갯수
maximum = -1
# 기타 치는 사람 수
person_count = -1

# [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]과 같이 bit 연산을 위한 준비
# 2^N개 입력받기
for idx in range(2 ** N):
    numbers = list()
    # 숫자 N개 입력해주기
    for j in range(1, N + 1):
        # print(f"idx: {idx}, j: {j}, 2**j: {2**j}, idx % 2**j: {(idx) % (2**j)}")
        if idx % (2 ** j) >= (2 ** (j - 1)):
            numbers.append(1)
        else:
            numbers.append(0)
    
    # 뒤집기
    numbers = numbers[::-1]
    
    # 방문 여부 확인
    visited = [0] * M

    # 사람 N명에 대한 탐색
    for i in range(N):
        # 기타 연주할 수 있는 사람이면 연주시키기
        if numbers[i] == 1:
            # 사람 i가 연주할수도 아닐수도 있는 곡 M개
            for j in range(M):
                # print(print(i, j, guitars[i][j]))
                # 만약 아직 연주하지 않았고 연주할 수 있는 곡이라면 visited 처리
                if visited[j] == 0 and guitars[i][j] == 'Y':
                    visited[j] = 1
    
    # print(numbers, visited)
    # print(sum(visited), maximum, sum(numbers), person_count)
    # 연주한 곡이 없다면 continue
    if sum(visited) == 0:
        continue
    # 지금 연주한 곡 수가 최고치를 경신했다면
    if sum(visited) > maximum:
        # 최고치 재기록
        maximum = sum(visited)
        # 연주한 사람 숫자 갱신
        person_count = sum(numbers)
    # 지금 연주한 곡 수가 타이 기록이고, 연주한 사람 수가 적다면
    elif sum(visited) == maximum and sum(numbers) < person_count:
        # 최고치 재기록
        maximum = sum(visited)
        # 연주한 사람 숫자 갱신
        person_count = sum(numbers)


# print(maximum)
# 사람 숫자 return
print(person_count)
# print(ans)
