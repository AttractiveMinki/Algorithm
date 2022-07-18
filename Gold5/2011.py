# 2011 암호코드

numbers = list(map(int, input()))
length = len(numbers)

i = 0
num = [1]
key = 1
if numbers[0] == 0:
    key = 0
while i + 1 < length:
    if numbers[i + 1] == 0 and (numbers[i] == 0 or numbers[i] >= 3):
        key = 0
        break
    if (numbers[i] == 1 and 0 < numbers[i + 1] <= 9) or (numbers[i] == 2 and 0 < numbers[i + 1] <= 6):
        cnt = 1
        
        while i + 1 < length and ((numbers[i] == 1 and 0 <= numbers[i + 1] <= 9) or (numbers[i] == 2 and 0 <= numbers[i + 1] <= 6)):
            cnt += 1
            i += 1
            # 1101 -> 0 만나면 -1
            if i + 1 < length and numbers[i + 1] == 0:
                # 2301
                cnt -= 1
                if numbers[i] >= 3:
                    key = 0
                break
            # 00 30 40 등등 cut
            if i + 1 < length and (numbers[i + 1] == 0 and (numbers[i] == 0 or numbers[i] >= 3)):
                key = 0
                break
        if key == 0:
            break
        num.append(cnt)
                  
    i += 1

if key == 0:
    print(0)
else:
    dp = [0] * (max(num) + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, max(num) + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    result = 1
    for idx in num:
        result *= dp[idx]
        result %= 1000000

    print(result)


"""
216510651510516520
1101
2301
00
30
40
121074110
1210
110
"""
