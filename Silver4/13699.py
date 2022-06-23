# 13699 점화식

n = int(input())

numbers = [1]
for _ in range(n):
    temp_num = 0
    for i in range(len(numbers)):
        num = numbers[i] * numbers[-i - 1]
        temp_num += num
    numbers.append(temp_num)
        
print(numbers[n])
