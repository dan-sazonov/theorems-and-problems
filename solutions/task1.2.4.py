x = list(map(int, input().split()))
x_max = 0

for i in x:
    if i > x_max:
        x_max = i

print(x_max)
# print(max(x)) - трушный питонячий путь
