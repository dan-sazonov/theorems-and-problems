a, n = map(int, input().split())
b = a

for _ in range(n - 1):
    b *= a

print(b)
