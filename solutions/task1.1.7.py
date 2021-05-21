a, d = map(int, input().split())
q0 = d
q = 0

while q0 < a:
    q0 += d
    q += 1

r = a - q * d
if r == d:
    r = 0
    q += 1

print(q, r)
