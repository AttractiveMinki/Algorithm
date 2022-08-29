# nCr
# N은 n, M은 r
# 5 3처럼 입력한다.

def comb(level, start):
    if level == M:
        print(comb_list)
        return

    for i in range(start, N):
        comb_list.append(i)
        comb(level + 1, i + 1)
        comb_list.pop()

N, M = map(int, input().split())
comb_list = list()
comb(0, 0)

"""
5 3
[0, 1, 2]
[0, 1, 3]
[0, 1, 4]
[0, 2, 3]
[0, 2, 4]
[0, 3, 4]
[1, 2, 3]
[1, 2, 4]
[1, 3, 4]
[2, 3, 4]

5 2
[0, 1]
[0, 2]
[0, 3]
[0, 4]
[1, 2]
[1, 3]
[1, 4]
[2, 3]
[2, 4]
[3, 4]
"""

# ## 덜 스마트한 방법 ##
# # level만 갖고 다녀도 되는 장점이 있지만, for문 안에서 if문을 한 번 더 써야하는 단점이 있다. #

# # nCr 구현
# def comb(level):
#     if level == M:
#         print(comb_list)
#         return
#     for i in range(level, N):
#         if comb_list == [] or comb_list[-1] < i:
#             comb_list.append(i)
#             comb(level + 1)
#             comb_list.pop()

# N, M = map(int, input().split())
# comb_list = list()
# comb(0)
