# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXb6Hvx6u1QDFARR&contestProbId=AXj2pzgaADkDFAS8&probBoxId=AXj2uot6AHUDFAS8&type=USER&problemBoxTitle=210422_Day28&problemBoxCnt=6
# 28일차 최소 신장 트리

# 5249(11946) 최소 신장 트리 - 제출용
 
def get_value():
    cnt = 0
     
    for number1, number2, weight in numbers:
        if find_nodes(number1) != find_nodes(number2):
            cnt += weight
            union(number1, number2)
    return cnt
 
# while 버전
def find_nodes(num):
    while num != roots[num]:
        num = roots[num]
    return num

# 재귀 버전
def find_nodes2(num):
    if num != roots[num]:
        roots[num] = find_nodes2(roots[num])
    return roots[num]
     
def union(root, node):
    roots[find_nodes(node)] = find_nodes(root)
 
 
T = int(input())
 
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    numbers = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
    roots = [i for i in range(E)]
 
    result = get_value()
     
    print('#%d %d' % (test_case, result))