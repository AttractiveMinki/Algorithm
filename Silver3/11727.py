# 11727 2×n 타일링 2

N = int(input())
numbers = [1]
for i in range(N - 1):
    if i % 2 == 1:
        numbers.append((numbers[-1] * 2 - 1) % 10007)
    else:
        numbers.append((numbers[-1] * 2 + 1) % 10007)

print(numbers[N - 1])

# N = int(input())
# num = 1
# for i in range(N - 1):
#     if i % 2 == 1:
#         num *= 2
#         num -= 1
#         num %= 10007
#     else:
#         num *= 2
#         num += 1
#         num %= 10007
# print(num)
