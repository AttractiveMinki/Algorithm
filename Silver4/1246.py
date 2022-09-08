import sys

sys.stdin = open('test.txt', 'r')

# 1246 온라인 판매

N, M = map(int, input().split())

numbers = sorted([int(input()) for _ in range(M)])

maximum = 0
result_value = 0
length = len(numbers)
for idx, num in enumerate(numbers):
    egg_cnt = length - idx
    if egg_cnt > N:
        egg_cnt = N
    cur_value = egg_cnt * num
    if cur_value > maximum:
        maximum = cur_value
        result_value = num
    # print(f"cnt: {egg_cnt}, num: {num}, cur_value: {cur_value}, maximum: {maximum}")
    
print(result_value, maximum)
    
"""
9% 틀렸습니다.
계란 갯수 제한을 두지 않음.

"""