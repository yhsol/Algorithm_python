def sum_n(n):
    return n * (n + 1) // 2


def fact(n):
    s = 0
    for i in range(1, n+1):
        s = s + (i * i)
    return s


def fact_n(n):
    return (n * (n+1) * (2*n+1)) // 6


print(fact_n(10))
