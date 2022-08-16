import sys

sys.stdin = open('test.txt', 'r')

# 1934 최소공배수

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    tA = A
    tB = B
    while tA != tB:
        if tA > tB:
            tB += B
        else:
            tA += A
    print(tA)
