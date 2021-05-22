# просите за квадрат - сделаю за квадрат. Идеальное решение см. в task1.2.5 или task1.2.7
x = list(map(int, input().split()))
n = len(x)
diff = n

for i in range(n):
    dec = 0
    for j in range(i + 1, n):
        if x[i] == x[j]:
            dec = 1
    diff -= dec

print(diff)
