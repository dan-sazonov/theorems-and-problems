n = int(input())
points = []
ans = 0
k = 0

for _ in range(n):
    a, b = map(int, input().split())
    points.extend([(a, 0), (b, 1)])
points.sort()

for _, edge in points:
    k -= 1 if edge else -1
    ans = k if k > ans else ans

print(ans)
