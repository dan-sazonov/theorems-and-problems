n = int(input())
points = []
ans = []
k = 0

for _ in range(n):
    a, b = map(int, input().split())
    points.extend([(a, 0), (b, 1)])
points.sort()

for _, edge in points:
    if edge:
        k -= 1
    else:
        k += 1
    ans.append(k)

print(max(ans))
