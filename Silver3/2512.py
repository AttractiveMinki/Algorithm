# 2512 예산

N = int(input())
moneys = sorted(list(map(int, input().split())))
M = int(input())

left = 0
right = moneys[-1]

ans = 0
while left <= right:
    mid = (left + right) // 2
    temp_ans = 0
    for money in moneys:
        temp_ans += min(mid, money)
    print(left, right, mid, ans, temp_ans, M)
    if temp_ans <= M:
        ans = max(mid, ans)
        left = mid + 1
    else:
        right = mid - 1
        
print(ans)
