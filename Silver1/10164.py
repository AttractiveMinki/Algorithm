import sys

sys.stdin = open('test.txt', 'r')

# 10164 격자상의 경로

def get_num(num):
    if num == 0:
        return 0, 0
    cur_num = 0
    for r in range(N):
        for c in range(M):
            cur_num += 1
            if cur_num == K:
                return r, c
    return 0, 0

N, M, K = map(int, input().split())
cur_r, cur_c = get_num(K)

# print(f"cur_r: {cur_r}, cur_c: {cur_c}")
total1 = cur_r + cur_c

result1 = 1
for i in range(total1, cur_r, -1):
    result1 *= i
for i in range(1, cur_c + 1):
    result1 //= i
# print(result1)

final_r = N - cur_r - 1
final_c = M - cur_c - 1
total2 = final_r + final_c

result2 = 1
for i in range(total2, final_r, -1):
    result2 *= i
for i in range(1, final_c + 1):
    result2 //= i

# print(result2)

# print(f"total1: {total1}, result1: {result1}")
# print(f"total2: {total2}, result2: {result2}")

if result1 == 0:
    result = result2
elif result2 == 0:
    result = result1
else:
    result = result1 * result2
print(result)
