def find_max(a):
    n = len(a)
    max_v = 0
    for i in range(1, n):
        if a[i] < a[max_v]:
            max_v = i
    return a[max_v]

v = [17,92,1,18,33,58,7,33,42,8,6]
print(find_max(v))
