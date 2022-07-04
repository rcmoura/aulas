def primos(n):
    p = 1
    yield 2
    d = 3
    b = 3
    while p < n:
        if b % d == 0:
            if b == d:
                yield b
                p += 1
            b += 2
        elif d < b:
            d += 2
        else:
            b += 2

for primo in primos(400):
    print(primo)