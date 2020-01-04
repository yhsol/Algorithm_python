def find(a):
    s = 0
    for i in range(1, a+1):
        b = i*i
        s = s + b
    return s


def find2(c):
    return c * (c+1) * (2 * c + 1) // 6


print(find(100))
print(find2(100))
