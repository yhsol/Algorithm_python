def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


data = int(input())
print(sum_n(data))
