# 16564 히오스 프로게이머

N, K = map(int, input().split())
numbers = list()
for _ in range(N):
    num = int(input())
    numbers.append(num)
    
# 숫자 정렬
numbers.sort()
# 현재 보고 있는 idx
idx = 0
# idx 이동기준이 되는 숫자
pivot_num = numbers[0]

# numbers 길이
length = len(numbers)
# K가 양수일 때 진행
while K > 0:
    # idx가 끝에 다다랐다면
    if idx == length - 1:
        # pivot_num이 numbers보다 크면, idx + 1을 더해준다.
        if pivot_num >= numbers[idx]:
            K -= (idx + 1)
        else:
            K -= idx
    # idx가 아직 끝에 다다르지 않았다면
    else:
        # 연산 중간에 끝에 다다랐을 경우를 표시
        key = 0
        # 기준 숫자보다 현재 숫자가 작거나 같다면
        while pivot_num >= numbers[idx]:
            # 만약 끝에 다다랐다면
            if idx == length - 1:
                # key 바꿔줌
                key = 1
                break
            # idx를 하나 늘려준다.
            idx += 1
        # 끝에 다다른게 아니라면
        if key == 0:
            K -= (idx)
        # 끝에 다다랐다면
        else:
            # pivot_num이 numbers보다 크면, idx + 1을 더해준다.
            if pivot_num >= numbers[idx]:
                K -= (idx + 1)
            else:
                K -= idx
    # K가 음수면 pivot_num 추가하지 않음
    if K < 0:
        break
    # pivot_num 추가해줌.
    pivot_num += 1
        
print(pivot_num)


### 숙련된 조교

# N, K = map(int, input().split())
# A = sorted([int(input()) for _ in range(N)])
# key = 0
# for i in range(N-1):
#     g = A[i+1] - A[i]
#     ck = g * (i+1)
#     print(f"i: {i}, i+1, i의 차이 g: {g}, 차이 * (i + 1) ck: {ck}, K: {K}")
#     if K >= ck:
#         K-= ck
#         continue
#     # K가 음수
#     else:
#         key = 1
#         print(A[i] + K//(i+1))
#         print(f"i: {i}, K: {K}")
#         break
# # K 살아있음
# if key == 0:
    
#     print('나왔쥬')
#     print(A[N-1] + K//N)
#     print(f"K: {K}, N: {N}")
