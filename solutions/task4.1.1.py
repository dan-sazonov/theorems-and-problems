# бабл-сорт, без оптимизации

x = list(map(int, input().split()))
unordered = True

while unordered:
    unordered = False
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = x[i + 1], x[i]
            unordered = True

print(*x)
