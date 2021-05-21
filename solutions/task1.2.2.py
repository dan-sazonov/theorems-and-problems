x = list(map(int, input().split()))

k = len(list(filter(lambda foo: foo == 0, x)))

print(k)
