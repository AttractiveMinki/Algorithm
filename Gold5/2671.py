import sys

sys.stdin = open('test.txt', 'r')

# 2671 잠수함 식별

N = input()

idx = 0
key = 1
prev_idx = -1
while idx < len(N):
    # 100~1~
    if N[idx] == '1':
        # 00
        idx += 1
        if idx >= len(N) or N[idx] != '0':
            key = 0
            break
        idx += 1
        if idx >= len(N) or N[idx] != '0':
            key = 0
            break
        # 0~
        while idx < len(N):
            if N[idx] == '0':
                idx += 1
            else:
                break
        # 1
        if idx >= len(N) or N[idx] != '1':
            key = 0
            break
        # 1~
        while idx < len(N):
            if N[idx] == '1':
                idx += 1
            else:
                break
    # 01
    else:
        # 0만 있으면 break
        if idx + 1 >= len(N):
            key = 0
            break
        # 앞의 1 땡겨와서 연산 할 수 있다면 ex) 10000111001111
        elif idx > 1 and idx + 2 < len(N) and N[idx + 1] == '0' and N[idx - 1] == '1' and N[idx - 2] == '1':
            idx -= 1
        else:
            while idx + 1 < len(N):
                if N[idx] == '0' and N[idx + 1] == '1':
                    idx += 2
                else:
                    break

    if prev_idx == idx:
        key = 0
        break
    prev_idx = idx

if key == 0:
    print('NOISE')
else:
    print('SUBMARINE')

# 5% 반례
# 100001001111 (prev_idx == idx 없을 때 while 탈출 못하는 반례이기도 함)
# 중간의 1을 앞에서도 쓰고 뒤에서도 쓴다.

# 17% 반례
# 01010110001100010101101
# 100010101101
# 01101
# 01 뒤에 1001이 있는지 없는지 판별 불가
# while 안에서 else - else - else 안에 idx += 1 했을 때 발생.
