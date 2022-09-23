import sys

sys.stdin = open('test.txt', 'r')

# 5373 큐빙

# 좌측 반시계 방향
def left_minus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 좌측 반시계 방향으로 돌리기
    for r in range(3, 6):
        for c in range(3):
            cubics[r][c] = temp_cubics[c + 3][5 - r]

    # 인접한 것들도 돌려주기
    for r in range(12):
        cubics[r][3] = temp_cubics[(r + 3) % 12][3]

    return


# 좌측 시계방향
def left_plus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 좌측 시계 방향으로 돌리기
    for r in range(3, 6):
        for c in range(3):
            cubics[r][c] = temp_cubics[5 - c][r - 3]
    
    # 인접한 것들도 돌려주기
    for r in range(12):
        cubics[r][3] = temp_cubics[(r - 3) % 12][3]

    return


# 위쪽 반시계방향
def up_minus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 위쪽 반시계 방향으로 돌리기
    for r in range(3):
        for c in range(3, 6):
            cubics[r][c] = temp_cubics[c - 3][5 - r]

    # 인접한 것들도 돌려주기
    cubics[3][0] = temp_cubics[11][5]
    cubics[3][1] = temp_cubics[11][4]
    cubics[3][2] = temp_cubics[11][3]
    for c in range(3, 9):
        cubics[3][c] = temp_cubics[3][c - 3]
    cubics[11][3] = temp_cubics[3][8]
    cubics[11][4] = temp_cubics[3][7]
    cubics[11][5] = temp_cubics[3][6]

    return


# 위쪽 시계방향
def up_plus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 위쪽 시계 방향으로 돌리기
    for r in range(3):
        for c in range(3, 6):
            cubics[r][c] = temp_cubics[5 - c][r + 3]

    # 인접한 것들도 돌려주기
    for c in range(6):
        cubics[3][c] = temp_cubics[3][c + 3]
    cubics[3][6] = temp_cubics[11][5]
    cubics[3][7] = temp_cubics[11][4]
    cubics[3][8] = temp_cubics[11][3]
    cubics[11][3] = temp_cubics[3][2]
    cubics[11][4] = temp_cubics[3][1]
    cubics[11][5] = temp_cubics[3][0]

    return


# 앞쪽 반시계 방향
def front_minus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 앞쪽 반시계 방향으로 돌리기
    for r in range(3, 6):
        for c in range(3, 6):
            cubics[r][c] = temp_cubics[c][8 - r]

    # 인접한 것들도 돌려주기
    cubics[2][3] = temp_cubics[3][6]
    cubics[2][4] = temp_cubics[4][6]
    cubics[2][5] = temp_cubics[5][6]

    cubics[3][6] = temp_cubics[6][5]
    cubics[4][6] = temp_cubics[6][4]
    cubics[5][6] = temp_cubics[6][3]

    cubics[6][5] = temp_cubics[5][2]
    cubics[6][4] = temp_cubics[4][2]
    cubics[6][3] = temp_cubics[3][2]

    cubics[5][2] = temp_cubics[2][3]
    cubics[4][2] = temp_cubics[2][4]
    cubics[3][2] = temp_cubics[2][5]

    return


# 앞쪽 시계 방향
def front_plus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 앞쪽 반시계 방향으로 돌리기
    for r in range(3, 6):
        for c in range(3, 6):
            cubics[r][c] = temp_cubics[8 - c][r]

    # 인접한 것들도 돌려주기
    cubics[2][3] = temp_cubics[5][2]
    cubics[2][4] = temp_cubics[4][2]
    cubics[2][5] = temp_cubics[3][2]

    cubics[5][2] = temp_cubics[6][5]
    cubics[4][2] = temp_cubics[6][4]
    cubics[3][2] = temp_cubics[6][3]

    cubics[6][5] = temp_cubics[3][6]
    cubics[6][4] = temp_cubics[4][6]
    cubics[6][3] = temp_cubics[5][6]

    cubics[3][6] = temp_cubics[2][3]
    cubics[4][6] = temp_cubics[2][4]
    cubics[5][6] = temp_cubics[2][5]

    return


# 우쪽 반시계 방향
def right_minus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 위쪽 반시계 방향으로 돌리기
    for r in range(3, 6):
        for c in range(6, 9):
            cubics[r][c] = temp_cubics[c - 3][11 - r]

    # 인접한 것들도 돌려주기
    for r in range(12):
        cubics[r][5] = temp_cubics[(r - 3) % 12][5]

    return


# 우측 시계방향
def right_plus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 좌측 시계 방향으로 돌리기
    for r in range(3, 6):
        for c in range(6, 9):
            cubics[r][c] = temp_cubics[11 - c][r + 3]
    
    # 인접한 것들도 돌려주기
    for r in range(12):
        cubics[r][5] = temp_cubics[(r + 3) % 12][5]

    return


# 아래쪽 반시계방향
def down_minus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 위쪽 반시계 방향으로 돌리기
    for r in range(6, 9):
        for c in range(3, 6):
            cubics[r][c] = temp_cubics[3 + c][11 - r]

    # 인접한 것들도 돌려주기
    for c in range(6):
        cubics[5][c] = temp_cubics[5][c + 3]
    cubics[5][6] = temp_cubics[9][5]
    cubics[5][7] = temp_cubics[9][4]
    cubics[5][8] = temp_cubics[9][3]

    cubics[9][5] = temp_cubics[5][0]
    cubics[9][4] = temp_cubics[5][1]
    cubics[9][3] = temp_cubics[5][2]

    return


# 아래쪽 시계방향
def down_plus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 위쪽 반시계 방향으로 돌리기
    for r in range(6, 9):
        for c in range(3, 6):
            cubics[r][c] = temp_cubics[11 - c][r - 3]

    # 인접한 것들도 돌려주기
    cubics[5][0] = cubics[9][5]
    cubics[5][1] = cubics[9][4]
    cubics[5][2] = cubics[9][3]
    for c in range(3, 9):
        cubics[5][c] = temp_cubics[5][c - 3]

    cubics[9][3] = temp_cubics[5][8]
    cubics[9][4] = temp_cubics[5][7]
    cubics[9][5] = temp_cubics[5][6]

    return


# 뒤쪽 반시계방향
def back_minus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 위쪽 반시계 방향으로 돌리기
    for r in range(9, 12):
        for c in range(3, 6):
            cubics[r][c] = temp_cubics[6 + c][14 - r]

    # 인접한 것들도 돌려주기
    cubics[8][3] = temp_cubics[5][8]
    cubics[8][4] = temp_cubics[4][8]
    cubics[8][5] = temp_cubics[3][8]

    cubics[5][8] = temp_cubics[0][5]
    cubics[4][8] = temp_cubics[0][4]
    cubics[3][8] = temp_cubics[0][3]

    cubics[0][5] = temp_cubics[3][0]
    cubics[0][4] = temp_cubics[4][0]
    cubics[0][3] = temp_cubics[5][0]

    cubics[3][0] = temp_cubics[8][3]
    cubics[4][0] = temp_cubics[8][4]
    cubics[5][0] = temp_cubics[8][5]

    return


# 뒤쪽 시계방향
def back_plus():
    # cubics 복사할 temp_cubics 선언
    temp_cubics = [cu[:] for cu in cubics]

    # 위쪽 시계 방향으로 돌리기
    for r in range(9, 12):
        for c in range(3, 6):
            cubics[r][c] = temp_cubics[14 - c][r - 6]

    # 인접한 것들도 돌려주기
    cubics[8][3] = temp_cubics[3][0]
    cubics[8][4] = temp_cubics[4][0]
    cubics[8][5] = temp_cubics[5][0]

    cubics[3][0] = temp_cubics[0][5]
    cubics[4][0] = temp_cubics[0][4]
    cubics[5][0] = temp_cubics[0][3]

    cubics[0][5] = temp_cubics[5][8]
    cubics[0][4] = temp_cubics[4][8]
    cubics[0][3] = temp_cubics[3][8]

    cubics[5][8] = temp_cubics[8][3]
    cubics[4][8] = temp_cubics[8][4]
    cubics[3][8] = temp_cubics[8][5]
    
    return


# initialize cubics
cubics = list()
cubics.append(['0'] * 3 + ['w'] * 3 + ['0'] * 3)
cubics.append(['0'] * 3 + ['w'] * 3 + ['0'] * 3)
cubics.append(['0'] * 3 + ['w'] * 3 + ['0'] * 3)
cubics.append(['g'] * 3 + ['r'] * 3 + ['b'] * 3)
cubics.append(['g'] * 3 + ['r'] * 3 + ['b'] * 3)
cubics.append(['g'] * 3 + ['r'] * 3 + ['b'] * 3)
cubics.append(['0'] * 3 + ['y'] * 3 + ['0'] * 3)
cubics.append(['0'] * 3 + ['y'] * 3 + ['0'] * 3)
cubics.append(['0'] * 3 + ['y'] * 3 + ['0'] * 3)
cubics.append(['0'] * 3 + ['o'] * 3 + ['0'] * 3)
cubics.append(['0'] * 3 + ['o'] * 3 + ['0'] * 3)
cubics.append(['0'] * 3 + ['o'] * 3 + ['0'] * 3)

original_cubics = [cu[:] for cu in cubics]

N = int(input())
for _ in range(N):
    cubics = [original[:] for original in original_cubics]
    method = int(input())
    rotate = list(input().split())

    for ro in rotate:
        if ro == 'L-':
            left_minus()
        elif ro == 'L+':
            left_plus()
        elif ro == 'U-':
            up_minus()
        elif ro == 'U+':
            up_plus()
        elif ro == 'F-':
            front_minus()
        elif ro == 'F+':
            front_plus()
        elif ro == 'R-':
            right_minus()
        elif ro == 'R+':
            right_plus()
        elif ro == 'B-':
            back_minus()
        elif ro == 'B+':
            back_plus()
        elif ro == 'D-':
            down_minus()
        elif ro == 'D+':
            down_plus()
            
    ans = list()
    for r in range(3):
        temp = list()
        for c in range(3, 6):
            temp.extend(cubics[r][c])
        ans.append(temp)

    for an in ans:
        print(''.join(an))


"""
기본 아이디어
0 w 0
g r b
0 y 0
0 o 0
위처럼 이중리스트를 만들고, 조건에 맞도록 해당 면과 주변 면을 돌려주었다.

처음 시도
첫 줄 0 w 0을 Index 0번, 둘째 줄 g r b를 Index 1번, ... 하는 식으로
삼중 리스트를 만들어 풀려고 했다.

마주친 문제점
삼중 리스트라서 리스트를 복제해주는 것이 쉽지 않았다.
복제는 어떻게어떻게 했지만.. 삼중 리스트가 불편해서, 다음과 같이 이중 리스트로 변경했다.

cubics = [['0'] * 3 + ['w'] * 3 + ['0'] * 3] * 3 + [['g'] * 3 + ['r'] * 3 + ['b'] * 3] * 3 + [['0'] * 3 + ['y'] * 3 + ['0'] * 3] * 3 + [['0'] * 3 + ['o'] * 3 + ['0'] * 3] * 3
다만 이렇게  cubics를 설정했을 때,
cubics[4][0]의 값을 변경하면, cubics[5][0]과 cubics[6][0]의 값도 같이 변경되는 문제점을 발견했다.
['0'] * 3 + ['w'] * 3 + ['0'] * 3]에 *3을 해줘서 주소 값이 복사된 것으로 판단하고, 다소 무식하게 초기화를 시켰다.

정해진 면을 시계/반시계 방향으로 돌린 뒤에, 그 주변 면들을 돌려주는 아이디어를 생각하는 것이 어려웠다.

아래 부분을 돌릴 때, 주변 큐빙을 어떻게 돌려줘야 하는지 생각해내는 게 매우 어려웠다.
전개도를 그려가며 겨우 해결했다.

down에서 주변 큐빙 값을 돌릴 때
아래쪽 면을 돌려 밑 면도 같이 돌릴 때 11행 값을 돌려주면 된다고 생각했는데, 예제 2번에서 자꾸 잘못된 값이 나왔다.
알고보니, 9행 값을 돌려줘야 했다.

50% Index Error
R- 에서, r의 range를 0~3으로 설정해서 에러가 발생했다.
r의 range를 3~6으로 바꿔주니, 문제가 해결되었다.

큐빙 문제가 어렵다는 평을 많이 들었는데, 직접 풀어보니 공간적인 감각이 많이 필요하고, 매우 많은 시간이 소요되는 문제였다.
한 문제를 푸는 데에 3시간 좀 안되게 걸렸다.
긴장을 많이 하고 있을 시험장에서 이 문제를 한 시간 반(이번 하반기부터는 2시간) 내에 풀어내는 것은 쉽지 않을 것 같다.
더 많은 연습을 해야겠다.
"""
