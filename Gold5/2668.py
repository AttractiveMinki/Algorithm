import sys

sys.stdin = open('test.txt', 'r')

# 2668 숫자 고르기

N = int(input())
numbers = [0] + [int(input()) for _ in range(N)]
# print(numbers)

total_visit_num = set()
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    queue = [numbers[i]]
    visit_num = list()
    while queue:
        cur_num = queue.pop()
        if visited[cur_num] == 1:
            continue
        visited[cur_num] = 1
        visit_num.append(cur_num)
        queue.append(numbers[cur_num])
    # print(f"i: {i}")
    # print(f"visited: {visited}")
    # print(f"visit_num: {visit_num}")
    if visited[i] == 1:
        for vi in visit_num:
            total_visit_num.add(vi)
    # print(total_visit_num)

total_visit_num = sorted(list(total_visit_num))
print(len(total_visit_num))
for to in total_visit_num:
    print(to)

# 8% 틀렸습니다.
# set으로 설정 -> 정렬 자동으로 되지 않음.
# 마지막에 list로 바꾼 뒤 sorted로 정렬해줌.