# 16401 과자 나눠주기

def check_cnt(mid):
    cnt = 0
    for number in numbers:
        cnt += (number // mid)

    if cnt >= M:
        maximum[0] = max(mid, maximum[0])
        return True
    else:
        return False
    

M, N = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

maximum = [0]
start = 1
end = numbers[-1]
mid = (start + end) // 2
result = check_cnt(mid)

while start < end:
    # cnt 이상, start = mid + 1
    if result == True:
        start = mid + 1
        mid = (start + end) // 2
    # cnt 미만, end = mid - 1
    else:
        end = mid - 1
        mid = (start + end) // 2
    result = check_cnt(mid)
    
print(maximum[0])


# maximum[0] 대신 maximum을 사용하면 시간초과가 난다.. 
# -> 함수에 불필요하게 들어가던 argument인 start, end를 제거해주니 돌아간다.
# -> 4256ms -> 4956ms가 소요되어, 더 많은 시간이 걸렸다.
# maximum을 사용할 때엔, check_cnt function 안쪽에서 계산하지 않고, if result == True일 때 계산하고,
# print(maximum) 이전에 if result == True: maximum = max(mid, maximum)을 추가하였다.
# pypy에선 maximum[0]보다 maximum의 실행 시간이 빨랐다. 메모리는 262436KB로 똑같았다.

# def check_cnt에서 함수의 원래 이름은 recur였다.
# recur -> check_cnt로 이름을 바꾸니 실행 시간이 4064ms -> 4256ms로 늘어났다. 기분 탓인가..

### 4956ms 코드

# 16401 과자 나눠주기

def check_cnt(mid):
    cnt = 0
    for number in numbers:
        cnt += (number // mid)

    if cnt >= M:
        
        return True
    else:
        return False
    

M, N = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

maximum = 0
start = 1
end = numbers[-1]
mid = (start + end) // 2
result = check_cnt(mid)

while start < end:
    # cnt 이상, start = mid + 1
    if result == True:
        maximum = max(mid, maximum)
        start = mid + 1
        mid = (start + end) // 2
    # cnt 미만, end = mid - 1
    else:
        end = mid - 1
        mid = (start + end) // 2
    result = check_cnt(mid)
    
if result == True:
    maximum = max(mid, maximum)
    
print(maximum)
