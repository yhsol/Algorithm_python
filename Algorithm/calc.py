def find(a, n):
    if n <= 1:
        return a[0]
    s_n_1 = find(a, n-1)
    if s_n_1 > a[n-1]:
        return s_n_1
    else:
        return a[n-1]


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find(v, len(v)))


# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-2) + fibo(n-1)


# print(fibo(7))
