import bisect

arr = list(map(int, input().split()))
# arr = [0, 1, 1, 1, 2, 3, 4, 3, 4, 4, 5]
diff = 0

for i in arr:
    if bisect.bisect_right(arr, i) - bisect.bisect_left(arr, i) == 1:
        diff += 1

print(diff)
