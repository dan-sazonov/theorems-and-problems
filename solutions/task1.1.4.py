a, n = map(int, input().split())


def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        b = power(a, n / 2)
        return b * b
    else:
        return power(a, n - 1) * a


print(power(a, n))
