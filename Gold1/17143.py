# 17143 낚시왕

R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]

# 속력 조절
for idx in range(M):
    # 위나 아래로 간다면
    if sharks[idx][3] == 1 or sharks[idx][3] == 2:
        # 속력
        sharks[idx][2] %= (R - 1) * 2

    #  왼쪽이나 오른쪽으로 간다면
    if sharks[idx][3] == 3 or sharks[idx][3] == 4:
        # 속력
        sharks[idx][2] %= (C - 1) * 2

total = 0
for i in range(1, C+1): #열
    min_length = 101
    target = -1
    for j in range(1, R+1): #행
        for idx in range(M):
            if sharks[idx][1] == i:
                if min_length > sharks[idx][0]:
                    min_length = sharks[idx][0]
                    target = idx
    if target != -1: # 해당 열에 상어가 있으면
        total += sharks[target][4]
        sharks[target][0], sharks[target][1] = 0, 0 # 사라짐
    
    # 상어 이동하기
    # 1 위, 2 아래, 3 오른쪽, 4 왼쪽
    for idx in range(M):
        # 상어가 존재하는 경우
        if sharks[idx][0] != 0 and sharks[idx][1] != 0:
            energy = sharks[idx][2]

            # edge case 방향 미리 설정
            if sharks[idx][0] == 1 and sharks[idx][3] == 1:
                sharks[idx][3] = 2
            elif sharks[idx][0] == R and sharks[idx][3] == 2:
                sharks[idx][3] = 1
            elif sharks[idx][1] == 1 and sharks[idx][3] == 4:
                sharks[idx][3] = 3
            elif sharks[idx][1] == C and sharks[idx][3] == 3:
                sharks[idx][3] = 4
            
            #이동
            while energy:
                # 위 방향이라면
                if sharks[idx][3] == 1:
                    # 행을 하나 감소
                    sharks[idx][0] -= 1
                    energy -= 1
                    # 만약 맨 위에 도착했다면
                    if sharks[idx][0] == 1:
                        # 상어의 방향을 바꿈
                        sharks[idx][3] = 2
                        
                # 아래 방향이라면
                elif sharks[idx][3] == 2:
                    # 행을 하나 증가
                    sharks[idx][0] += 1
                    energy -= 1
                    # 만약 맨 아래에 도착했다면
                    if sharks[idx][0] == R:
                        # 상어의 방향을 바꿈
                        sharks[idx][3] = 1
                        
                # 오른쪽 방향이라면
                elif sharks[idx][3] == 3:
                    # 열을 하나 증가
                    sharks[idx][1] += 1
                    energy -= 1
                    # 만약 맨 왼쪽에 도착했다면
                    # 만약 맨 오른에 도착했다면
                    if sharks[idx][1] == C:
                        # 상어의 방향을 바꿈
                        sharks[idx][3] = 4
            
                # 왼쪽 방향이라면
                elif sharks[idx][3] == 4:
                    # 열을 하나 감소
                    sharks[idx][1] -= 1
                    energy -= 1
                    # 만약 맨 왼쪽에 도착했다면
                    if sharks[idx][1] == 1:
                        # 상어의 방향을 바꿈
                        sharks[idx][3] = 3
                        
    catch_list = [[[0, 0] for _ in range(C + 1)] for _ in range(R + 1)]
    # 잡아먹기
    for idx in range(M):
        # 상어가 존재하는 경우
        if sharks[idx][0] != 0 and sharks[idx][1] != 0:
            # catch_list가 비어있으면 넣기
            if catch_list[sharks[idx][0]][sharks[idx][1]][1] == 0:
                catch_list[sharks[idx][0]][sharks[idx][1]][0] = idx
                catch_list[sharks[idx][0]][sharks[idx][1]][1] = sharks[idx][4]        
            # 있으면 결투
            else:
                # 새로 들어온 것이 크면
                if catch_list[sharks[idx][0]][sharks[idx][1]][1] < sharks[idx][4]:
                    # 교체, 원래 상어의 r, c 0으로
                    sharks[catch_list[sharks[idx][0]][sharks[idx][1]][0]][0] = 0 # 사라짐
                    sharks[catch_list[sharks[idx][0]][sharks[idx][1]][0]][1] = 0 
                    catch_list[sharks[idx][0]][sharks[idx][1]][0] = idx
                    catch_list[sharks[idx][0]][sharks[idx][1]][1] = sharks[idx][4] 
                
                # 원래 있던 것이 크면
                else:
                    sharks[idx][0], sharks[idx][1] = 0, 0 # 사라짐

print('%d' % (total))
                