# 1802 종이 접기

def recur(N, start_idx, end_idx):
    if end_idx - start_idx <= 1:
        return
    
    length = end_idx - start_idx + 1
    mid_idx = (end_idx + start_idx) // 2
    
    # 중앙 값이면 return
    if mid_idx == N:
        return
    
    # idx가 범위 내에 없으면 return
    if start_idx > N or N > end_idx:
        return
    
    # 오른쪽
    if N > mid_idx:
        compare_num = N - (N - mid_idx) * 2
    # 왼쪽
    elif N < mid_idx:
        compare_num = N + (mid_idx - N) * 2
    else:
        return

    if numbers[compare_num] == numbers[N] and compare_num != N:
        result[0] = False
        return
    else:
        # 범위 안에 있으면
        if start_idx <= N <= end_idx:
            recur(N, start_idx, mid_idx - 1)
            recur(N, mid_idx + 1, end_idx)


T = int(input())

for _ in range(T):
    numbers = list(input())
    length = len(numbers)
    result = [True]
    
    for i in range(len(numbers)):
        recur(i, 0, length - 1)
        if result[0] == False:
            break
    if result[0] == True:
        print('YES')
    else:
        print('NO')
