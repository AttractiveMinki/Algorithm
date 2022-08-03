# 11726 2xn 타일링

N = int(input())
numbers = [0, 1, 2]
for _ in range(N - 2):
    num = (numbers[-1] + numbers[-2]) % 10007
    numbers.append(num)
    
print(numbers[N])
