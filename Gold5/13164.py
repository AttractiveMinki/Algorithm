# 13164 행복 유치원

N, K = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

diff = list()
for i in range(len(numbers) - 1):
    diff.append(numbers[i + 1] - numbers[i])
diff.sort()

for _ in range(K - 1):
    diff.pop()
print(sum(diff))
