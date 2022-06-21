# 13305 주유소

N = int(input())
roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

minimum = 9876543210

for i in range(len(oils)):
    if minimum > oils[i]:
        minimum = oils[i]
    else:
        oils[i] = minimum

result = 0
for i in range(len(roads)):
    result += (roads[i] * oils[i])
    
print(result)
