a, b = map(int, input().split())

a += b
b = a - b
a -= b

print(a, b)
