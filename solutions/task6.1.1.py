arr = map(int, input().split())
ans = []

for i in arr:
    if i > 0:
        ans.append(i)
        continue
    if not ans and i < 0:
        print('no')
        break
    if ans and abs(ans[-1]) == abs(i):
        ans.pop()

print('no' if ans else 'yes')
