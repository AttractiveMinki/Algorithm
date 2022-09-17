import sys

sys.stdin = open('test.txt', 'r')

# 17140 이차원 배열

r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]

ans = -1
for i in range(101): # 101
    # 예제 6, 변환 과정에서 r, c 값이 없을 수도 있다.
    if len(matrix) >= r and len(matrix[0]) >= c and matrix[r-1][c-1] == k:
        ans = i
        break

    # r >= c
    if len(matrix) >= len(matrix[0]):
        temp_matrix = list()
        for mr in range(len(matrix)):
            temp_dict = dict()
            for mc in range(len(matrix[0])):
                cur_num = matrix[mr][mc]
                if cur_num == 0: # 0은 continue, 이거 안하면 예제 4에서 37나옴.
                    continue
                temp_dict[cur_num] = temp_dict.get(cur_num, 0) + 1
            temp_sort_list = list()
            for key in temp_dict:
                temp_sort_list.append([key, temp_dict[key]])
            
            temp_sort_list.sort(key=lambda x: (x[1], x[0])) # 조건에 맞게 정렬

            insert_list = list()
            # [[3, 1], [1, 2]] -> [3, 1, 1, 2]
            for te in temp_sort_list:
                insert_list.extend(te)
            temp_matrix.append(insert_list)

        maximum = 0
        for te in temp_matrix:
            maximum = max(len(te), maximum)

        # 최대 행 길이 100
        for i in range(min(len(temp_matrix), 100)):
            if len(temp_matrix[i]) < maximum:
                temp_matrix[i].extend([0] * (maximum - len(temp_matrix[i])))

        # 최대 열 길이 100
        matrix = [te[:100] for te in temp_matrix]

    # r < c
    else:
        temp_matrix = list()
        for mc in range(len(matrix[0])):
            temp_dict = dict()
            for mr in range(len(matrix)):
                cur_num = matrix[mr][mc]
                if cur_num == 0:
                    continue
                temp_dict[cur_num] = temp_dict.get(cur_num, 0) + 1
            temp_sort_list = list()
            for key in temp_dict:
                temp_sort_list.append([key, temp_dict[key]])

            temp_sort_list.sort(key=lambda x: (x[1], x[0])) # 조건에 맞게 정렬

            insert_list = list()
            # [[3, 1], [1, 2]] -> [3, 1, 1, 2]
            for te in temp_sort_list:
                insert_list.extend(te)
            temp_matrix.append(insert_list)

        maximum = 0
        for te in temp_matrix:
            maximum = max(len(te), maximum)

        # 최대 행 길이 100
        for i in range(min(len(temp_matrix), 100)):
            if len(temp_matrix[i]) < maximum:
                temp_matrix[i].extend([0] * (maximum - len(temp_matrix[i])))

        # r, c 바꿔주기
        rc_matrix = list()
        for temp_c in range(len(temp_matrix[0])):
            rc_temp = list()
            for temp_r in range(len(temp_matrix)):
                rc_temp.extend([temp_matrix[temp_r][temp_c]])
            # 최대 열 길이 100
            rc_matrix.append(rc_temp[:100])

        matrix = [te[:] for te in rc_matrix]

print(ans)


# 참고
# dictionary 정렬시 sorted 안에서 items() 사용하면 훨씬 쉽게 정렬 가능.

"""
my_dict = {1: 3, 2: 5, 3: 1, 4: 3}
print(my_dict)
my_dict = sorted(my_dict.items(), key=lambda x: (x[1], x[0]))
print(my_dict)
"""
# key=lambda x: (x[1], x[0])은 훌륭히 기억해냈으나
# dictionary 정렬시 items() 사용하면 되는 걸 잊어버림.. 반성..


### 주석 버전 ###

# # 17140 이차원 배열

# r, c, k = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(3)]

# ans = -1
# for i in range(101): # 101
#     # print(f"i: {i}")
#     # 예제 6, 변환 과정에서 r, c 값이 없을 수도 있다.
#     if len(matrix) >= r and len(matrix[0]) >= c and matrix[r-1][c-1] == k:
#         ans = i
#         break
#     # print("original matrix")
#     # for ma in matrix:
#     #     print(ma)

#     # r >= c
#     # print(f"len(matrix): {len(matrix)}, len(matrix[0]): {len(matrix[0])}")
#     if len(matrix) >= len(matrix[0]):
#         # print(f"### r >= c ###")
#         temp_matrix = list()
#         for mr in range(len(matrix)):
#             temp_dict = dict()
#             for mc in range(len(matrix[0])):
#                 cur_num = matrix[mr][mc]
#                 if cur_num == 0: # 0은 continue, 이거 안하면 예제 4에서 37나옴.
#                     continue
#                 temp_dict[cur_num] = temp_dict.get(cur_num, 0) + 1
#             temp_sort_list = list()
#             for key in temp_dict:
#                 temp_sort_list.append([key, temp_dict[key]])
            
#             # print(f"before: {temp_sort_list}")
#             temp_sort_list.sort(key=lambda x: (x[1], x[0])) # 조건에 맞게 정렬
#             # print(f"result: {temp_sort_list}")

#             insert_list = list()
#             # [[3, 1], [1, 2]] -> [3, 1, 1, 2]
#             for te in temp_sort_list:
#                 insert_list.extend(te)
#             temp_matrix.append(insert_list)

#         maximum = 0
#         for te in temp_matrix:
#             maximum = max(len(te), maximum)
#             # print(te, maximum)
#         # print(f"maximum: {maximum}")

#         # 최대 행 길이 100
#         for i in range(min(len(temp_matrix), 100)):
#             if len(temp_matrix[i]) < maximum:
#                 temp_matrix[i].extend([0] * (maximum - len(temp_matrix[i])))

#         # print(temp_matrix)
#         # 최대 열 길이 100
#         matrix = [te[:100] for te in temp_matrix]
#         # print(f"matrix:")
#         # for ma in matrix:
#         #     print(ma)
#         # print(matrix)
#     # r < c
#     else:
#         # print(f"### r < c ###")
#         temp_matrix = list()
#         for mc in range(len(matrix[0])):
#             temp_dict = dict()
#             for mr in range(len(matrix)):
#                 cur_num = matrix[mr][mc]
#                 if cur_num == 0:
#                     continue
#                 temp_dict[cur_num] = temp_dict.get(cur_num, 0) + 1
#             temp_sort_list = list()
#             for key in temp_dict:
#                 temp_sort_list.append([key, temp_dict[key]])

#             # print(f"before: {temp_sort_list}")
#             temp_sort_list.sort(key=lambda x: (x[1], x[0])) # 조건에 맞게 정렬
#             # print(f"result: {temp_sort_list}")

#             insert_list = list()
#             # [[3, 1], [1, 2]] -> [3, 1, 1, 2]
#             for te in temp_sort_list:
#                 insert_list.extend(te)
#             temp_matrix.append(insert_list)

#         maximum = 0
#         for te in temp_matrix:
#             maximum = max(len(te), maximum)
#             # print(te, maximum)
#         # print(f"maximum: {maximum}")
        
#         # 최대 행 길이 100
#         for i in range(min(len(temp_matrix), 100)):
#             if len(temp_matrix[i]) < maximum:
#                 temp_matrix[i].extend([0] * (maximum - len(temp_matrix[i])))

#         # r, c 바꿔주기
#         rc_matrix = list()
#         for temp_c in range(len(temp_matrix[0])):
#             rc_temp = list()
#             for temp_r in range(len(temp_matrix)):
#                 rc_temp.extend([temp_matrix[temp_r][temp_c]])
#             # 최대 열 길이 100
#             rc_matrix.append(rc_temp[:100])

#         # print(f"temp_matrix: {temp_matrix}")
#         # print(f"rc_matrix: {rc_matrix}")
#         matrix = [te[:] for te in rc_matrix]
#         # print(f"matrix:")
#         # for ma in matrix:
#         #     print(ma)
#         # print(matrix)

# # print(len(matrix))
# # print(len(matrix[0]))
# # for ma in matrix:
# #     print(ma)

# print(ans)
