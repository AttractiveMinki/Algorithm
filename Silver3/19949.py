# 19949 영재의 시험

def recur(level, cnt):
    # 문제 10개
    if level == 10:
        num[0] += 1
        return
    
    # 5지선다
    for i in range(1, 6):
        # 문제가 2개 이하거나 맨 뒤 숫자 두 개가 지금꺼와 다를 경우
        if len(numbers) < 2 or (numbers[-2] != numbers[-1] or numbers[-1] != i):
            numbers.append(i)
            # 정답 맞혔을 때
            if answer[len(numbers) - 1] == i:
                recur(level + 1, cnt + 1)
            else:
                # 남은 문제를 다 맞혀도 5개 이상이 될 수 없는 경우 - backtracking
                if len(numbers) - cnt > 5:
                    numbers.pop()
                    continue
                recur(level + 1, cnt)
            numbers.pop()

answer = list(map(int, input().split()))
numbers = list()
num = [0]
recur(0, 0)
print(num[0])
