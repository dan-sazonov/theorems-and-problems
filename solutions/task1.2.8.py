x = list(map(int, input().split()))
k = max(x)
count = [0] * (k + 1)

for i in x:
    count[i] += 1  # да, я знаю про collections.Counter

print(count)
