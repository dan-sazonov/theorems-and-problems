k = int(input())
n = int(input())
x = [1] * (k + 1)
last = [n] * (k + 1)
print(x)
while x != last:
    p = k
    while x[p - 1] < n:
        p -= 1
    x[p - 1] = x[p - 1] + 1
    for i in range(p + 1, k + 1):
        x[i] = 1
    print(x)
# print()
