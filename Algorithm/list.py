def find_max(a):
    n = len(a)
    pivot = a[0]
    for i in range(1, n):
        if a[i] > pivot:
            pivot = a[i]
    return pivot


def find_i(a):
    n = len(a)
    pivot = 0
    for i in range(1, n):
        if a[i] < a[pivot]:
            pivot = i
    return pivot


def find(a, n):
    if n == 1:
        return a[0]
    find_n_1 = find(a, n-1)
    if find_n_1 > a[n-1]:
        return find_n_1
    else:
        return a[n-1]


v = [17, 92, 18, 33, 58, 7, 33, 42]
result = find_max(v)
resulti = find_i(v)
results = find(v, len(v))
print(resulti)
print(v[resulti])
print(results)
