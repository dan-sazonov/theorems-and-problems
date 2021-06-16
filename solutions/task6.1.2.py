arr = map(int, input().split())
ans = 0

for i in arr:
    ans += i
    if ans < 0:
        print('no')
        break
else:
    print('no' if ans else 'yes')
