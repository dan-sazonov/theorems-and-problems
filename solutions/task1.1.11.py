n = int(input())
ans = 0


def fact(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


for j in range(0, n + 1):
    ans += 1 / fact(j)

print(ans)
