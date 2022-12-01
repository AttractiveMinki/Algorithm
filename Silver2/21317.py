import sys

sys.stdin = open('test.txt', 'r')

# 21317 징검다리 건너기

N = int(input())

numbers = list()
for idx in range(N - 1):
    small_E, big_E = map(int, input().split())
    numbers.append([small_E, big_E])
K = int(input())

queue = [[0, 0, 1]]
ans = 987654321
while queue:
    cur_idx, cur_value, cur_chance = queue.pop()
    if cur_idx >= N - 1:
        if cur_idx == N - 1:
            ans = min(cur_value, ans)
        continue
    # 한 칸
    queue.append([cur_idx + 1, cur_value + numbers[cur_idx][0], cur_chance])
    # 두 칸
    queue.append([cur_idx + 2, cur_value + numbers[cur_idx][1], cur_chance])
    if cur_chance == 1:
        queue.append([cur_idx + 3, cur_value + K, 0])

print(ans)


"""
queue = [[0, 0, 1]]
ans = 987654321
while queue:
    cur_idx, cur_value, cur_chance = queue.pop()
    print(f"cur_idx: {cur_idx}, cur_value: {cur_value}, cur_chance: {cur_chance}, len: {len(numbers)}")
    
    if cur_idx + 1 >= len(numbers):
        print(f"###renew ans, {cur_value}, {ans}###, {cur_idx}")
        print(f"{numbers[cur_idx][0]}, {numbers[cur_idx][1]}")
        ans = min(cur_value + numbers[cur_idx][0], cur_value + numbers[cur_idx][1], ans)
        if cur_chance == 1:
            ans = min(cur_value + K, ans)
        continue
    queue.append([cur_idx + 1, cur_value + numbers[cur_idx + 1][0], cur_chance])
    # if cur_idx + 1 < len(numbers):
    #     print(f"###renew ans, {cur_value + numbers[cur_idx + 1][0]}, {ans}###, {cur_idx}")
    #     ans = min(cur_value + numbers[cur_idx + 1][0], ans)
    if cur_idx + 2 < len(numbers):
        queue.append([cur_idx + 2, cur_value + numbers[cur_idx + 1][1], cur_chance])
        # if cur_idx + 2 < len(numbers):
        #     ans = min(cur_value + numbers[cur_idx + 1][1], ans)
    if cur_idx + 3 < len(numbers) and cur_chance == 1:
        cur_chance -= 1
        queue.append([cur_idx + 3, cur_value + K, cur_chance])
        # if cur_idx + 3 < len(numbers):
        #     ans = min(cur_value + K, ans)
    
    # 정답 갱신
    
    print(f"queue: {queue}")
        
print(ans)
"""
