# переменная k хранит количество первых отсортированных элементов

x = list(map(int, input().split()))
k = 0

for i in range(len(x) - 1):
    i_min = i
    print(x, k)
    for j in range(i + 1, len(x)):
        if x[j] < x[i_min]:
            i_min = j
    x[i_min], x[i] = x[i], x[i_min]
    k += 1

print(*x)
