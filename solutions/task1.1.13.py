# O(n)

a, b = map(int, input().split())
a_divs = set()
b_divs = set()

for i in range(1, a+1):
    if a % i == 0:
        a_divs.add(i)
for j in range(1, b+1):
    if b % j == 0:
        b_divs.add(j)

print(max(a_divs.intersection(b_divs)))
