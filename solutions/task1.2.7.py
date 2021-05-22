x = sorted(map(int, input().split()))
diff = 0

for i in range(1, len(x)):
    if x[i - 1] != x[i]:
        diff += 1

print(diff + 1)
