import sys

sys.stdin = open('test.txt', 'r')

# 1967 트리의 지름

N = int(input())
parents = dict() # 부모 -> 자식
childs = dict() # 자식 -> 부모
end_nums = set() # 자식이 없는 번호 모음
maxi_num = 0 # visited 만들기 위함

for _ in range(N - 1):
    parent, child, weight = map(int, input().split())
    end_nums.add(parent)
    end_nums.add(child)
    maxi_num = max(parent, child, maxi_num)

    if parent in parents:
        parents[parent].append([child, weight])
    else:
        parents[parent] = [[child, weight]]
    
    if child in childs:
        childs[child].append([parent, weight])
    else:
        childs[child] = [[parent, weight]]

# 끝 자식들부터 시작해서, 자식->부모->자식 탐색하며 maximum 값 찾기.
maximum = 0
maxi_num += 1
for num in end_nums:
    # 부모 찾기 위해 쓰는 list
    temp_num = [[num, 0]]
    # 부모 담는 임시 list
    temp_par = list()

    # 자식 -> 부모 보기
    visited = [0] * maxi_num
    visited[num] = 1
    while temp_num:
        temp, value = temp_num.pop()

        # 내가 누구의 childs면 다 추가
        if temp in childs:
            # print(f"childs[temp]: {childs[temp]}")
            for temp_child_num in childs[temp]:
                temp_num.append([temp_child_num[0], temp_child_num[1] + value])
                temp_par.append([temp_child_num[0], temp_child_num[1] + value])

        # 부모 -> 자식 보기
        while temp_par:
            temp, value = temp_par.pop()
            if visited[temp] == 1 and temp != 1:
                continue

            # 끝 숫자면 maximum 갱신
            if temp in end_nums:
                maximum = max(value, maximum)
            visited[temp] = 1

            # 내가 누구의 parents면 다 추가
            if temp in parents:
                for temp_parents_num in parents[temp]:
                    temp_par.append([temp_parents_num[0], temp_parents_num[1] + value])

print(maximum)



# # 1967 트리의 지름

# N = int(input())
# parents = dict() # 부모 -> 자식
# childs = dict() # 자식 -> 부모
# end_nums = set() # 자식이 없는 번호 모음
# maxi_num = 0 # visited 만들기 위함

# for _ in range(N - 1):
#     parent, child, weight = map(int, input().split())
#     end_nums.add(parent)
#     end_nums.add(child)
#     maxi_num = max(parent, child, maxi_num)

#     if parent in parents:
#         parents[parent].append([child, weight])
#     else:
#         parents[parent] = [[child, weight]]
    
#     if child in childs:
#         childs[child].append([parent, weight])
#     else:
#         childs[child] = [[parent, weight]]
    
# # print(end_nums)
# # for key in parents:
# #     # 부모 dict에 속하면(== child가 있으면) 제거하기
# #     if key in end_nums:
# #         end_nums.remove(key)

# print(end_nums)

# print(parents)
# print(childs)

# # 끝 자식들부터 시작해서, 자식->부모->자식 탐색하며 maximum 값 찾기.
# maximum = 0
# maxi_num += 1
# for num in end_nums:
#     # print(f"num: {num}")
#     # 부모 찾기 위해 쓰는 list
#     temp_num = [[num, 0]]
#     # 부모 담는 임시 list
#     temp_par = list()

#     # 자식 -> 부모 보기
#     visited = [0] * maxi_num
#     visited[num] = 1
#     while temp_num:
#         temp, value = temp_num.pop()
#         # print(f"temp: {temp}, value: {value}")
#         # 끝 숫자가 아니면 temp_par에 담기
#         # if temp not in end_nums:
#         #     temp_par.append([temp, value])

#         # 내가 누구의 childs면 다 추가
#         if temp in childs:
#             # print(f"childs[temp]: {childs[temp]}")
#             for temp_child_num in childs[temp]:
#                 temp_num.append([temp_child_num[0], temp_child_num[1] + value])
#                 temp_par.append([temp_child_num[0], temp_child_num[1] + value])
#                 # for idx, _ in parents[temp_child_num[0]]:
#                 #     temp_par.append([idx, temp_child_num[1] + value])
#                 #     # temp_par.append([parents[temp_child_num[0]][0][0], temp_child_num[1] + value])

#         # print(temp_num, temp)

#         # 부모 -> 자식 보기
#         print(f"temp_par: {temp_par}, num: {num}, temp: {temp}")
#         while temp_par:
#             temp, value = temp_par.pop()
#             if visited[temp] == 1:
#                 continue
#             # print(visited, temp, visited[temp])
#             # print(f"temp: {temp}, value: {value}")
#             # 끝 숫자면 maximum 갱신
#             if temp in end_nums:
#                 maximum = max(value, maximum)
#                 print(f"value: {value}, maximum: {maximum}, num: {num}, temp: {temp}")
#             visited[temp] = 1

#             # 내가 누구의 parents면 다 추가
#             if temp in parents:
#                 # print(f"parents[temp]: {parents[temp]}")
#                 for temp_parents_num in parents[temp]:
#                     temp_par.append([temp_parents_num[0], temp_parents_num[1] + value])

#         #     print(temp_par, temp)
#     # print(maximum)

# print(maximum)

