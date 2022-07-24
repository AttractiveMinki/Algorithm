# 1041 주사위

N = int(input())

numbers = list(map(int, input().split()))
if N == 1:
    numbers.sort()
    print(sum(numbers[:-1]))

else:
    minimum3 = min(numbers[0] + numbers[3] + numbers[4], numbers[0] + numbers[2] + numbers[4], numbers[0] + numbers[1] + numbers[2],
                  numbers[0] + numbers[1] + numbers[3], numbers[5] + numbers[3] + numbers[4], numbers[5] + numbers[2] + numbers[4],
                  numbers[5] + numbers[1] + numbers[2], numbers[5] + numbers[1] + numbers[3])

    minimum2 = min(numbers[0] + numbers[1], numbers[0] + numbers[2], numbers[0] + numbers[3], numbers[0] + numbers[4],
                  numbers[5] + numbers[1], numbers[5] + numbers[2], numbers[5] + numbers[3], numbers[5] + numbers[4],
                  numbers[1] + numbers[2], numbers[2] + numbers[4], numbers[4] + numbers[3], numbers[3] + numbers[1])
    minimum1 = min(numbers)

    if N == 2:
        print(minimum3 * 4 + minimum2 * 4)

    else:
        top = minimum3 * 4 + minimum2 * (4 * N - 8) + minimum1 * (N ** 2 - 4 * N + 4)
        mid = (N - 1) * (minimum2 * 4 + minimum1 * (4 * N - 8))
        print(top + mid)


"""
N = 1일 때
작은 5면의 수

N = 2일 때
작은 3개 * 4
작은 2개 * 4

N = 3일 때
맨 위
작은 3개 * 4
작은 2개 * 4
작은 1개 * 1

중간
작은 2개 * 4
작은 1개 * 4

아래
작은 2개 * 4
작은 1개 * 4

N = 4일 때
맨 위
작은 3개 * 4 (4)
작은 2개 * 8 (4 * N - 4 - 4) N줄 4개 - 코너 4개(중복) - 코너 4개(위에서 계산)
작은 1개 * 4 (N^2 - 4 * N + 4)

중간, 아래
작은 2개 * 4
작은 1개 * 8 (4 * N - 4 - 4)

N = k일 때
맨 위
작은 3개 * 4
작은 2개 * (4k - 8)
작은 1개 * (k^2 - 4*k + 4)

중간, 아래
작은 2개 * 4
작은 1개 * (4k - 8)


a b c d e f
1 2 3 4 5 6
0 1 2 3 4 5 (index)
작은 3개
a d e, a c e, a b c, a b d,
f d e, f c e, f b c, f b d
숫자로 치환
1 4 5, 1 3 5, 1 2 3, 1 2 4,
6 4 5, 6 3 5, 6 2 3, 6 2 4
index
0 3 4, 0 2 4, 0 1 2, 0 1 3,
5 3 4, 5 2 4, 5 1 2, 5 1 3

"""