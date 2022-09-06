import sys

sys.stdin = open('test.txt', 'r')

# 15683 감시

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def calc(camera_angle_idx):
    # print(f"camera_angle_idx: {camera_angle_idx}")
    temp_grounds = [gr[:] for gr in grounds]
    for camera_idx in range(camera_num):
        # print(f"camera_idx: {camera_idx}, camera_angle_idx: {camera_angle_idx[camera_idx]}, camera_position: {camera_position}")

        queue = list()
        # 카메라 위치, 카메라 종류
        cr, cc, ckind = camera_position[camera_idx]
        # 카메라 방향
        camera_direction = camera_angle_idx[camera_idx] % 4
        # print(f"camera_direction: {camera_direction}")
        # 직선 하나
        if ckind == 1:
            queue.append([cr, cc, camera_direction])
        # 직선, 맞은편
        elif ckind == 2:
            queue.append([cr, cc, camera_direction])
            queue.append([cr, cc, (camera_direction + 2) % 4])
        # 직선, 우측
        elif ckind == 3:
            queue.append([cr, cc, camera_direction])
            queue.append([cr, cc, (camera_direction + 1) % 4])
        # 직선, 우측, 맞은편
        elif ckind == 4:
            queue.append([cr, cc, camera_direction])
            queue.append([cr, cc, (camera_direction + 1) % 4])
            queue.append([cr, cc, (camera_direction + 2) % 4])
        # 네 방향
        elif ckind == 5:
            queue.append([cr, cc, camera_direction])
            queue.append([cr, cc, (camera_direction + 1) % 4])
            queue.append([cr, cc, (camera_direction + 2) % 4])
            queue.append([cr, cc, (camera_direction + 3) % 4])

        # 직선으로 나아가는 업무만 진행
        while queue:
            qr, qc, qdir = queue.pop()
            tr = qr + dr[qdir]
            tc = qc + dc[qdir]

            if 0 <= tr < N and 0 <= tc < M and temp_grounds[tr][tc] != 6:
                temp_grounds[tr][tc] = 7
                queue.append([tr, tc, qdir])
        
        cnt = 0
        for r in range(N):
            for c in range(M):
                if temp_grounds[r][c] == 0:
                    cnt += 1
        minimum_land[0] = min(cnt, minimum_land[0])


N, M = map(int, input().split())

grounds = [list(map(int, input().split())) for _ in range(N)]
camera_num = 0
camera_position = list()
temp_gr = 0
for r in range(N):
    for c in range(M):
        if 1 <= grounds[r][c] <= 5:
            camera_num += 1
            # 행, 열, 종류
            camera_position.append([r, c, grounds[r][c]])
        elif grounds[r][c] == 0:
            temp_gr += 1

if camera_num == 0:
    print(temp_gr)
else:
    minimum_land = [N * M]
    camera_angle_idx = [0] * camera_num

    for idx in range(4 ** camera_num):
        # print(f"idx: {idx}, idx % 4: {idx % 4}, idx // 4: {idx // 4}")
        camera_angle_idx[0] = idx % 4
        for i in range(1, camera_num):
            camera_angle_idx[i] = (idx // (4 ** i)) % 4
        # print(f"camera_angle_idx: {camera_angle_idx}")
        calc(camera_angle_idx)
    print(minimum_land[0])


"""
39% IndexError -> 카메라가 없을 때.. 고려하기
위 코드에서 if camera_num == 0 부분
"""
