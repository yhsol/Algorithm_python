
a = [17, 92, 18, 33, 58, 7, 33, 42]


def find_max(n):
    a = len(n)
    s = 0
    for i in range(1, a):
        if n[s] < n[i]:
            s = i
    return s


print(find_max(a))


def find_min(n):
    length = len(n)
    s = n[0]
    for i in range(1, length):
        if s > n[i]:
            s = n[i]
    return s


print(find_min(a))
