def factorial(n):
    s = 1
    for i in range(1, n+1):
        s = s * i
    return s


print(factorial(5))


def factorial_recursion(n):
    if n < 1:
        return 0
    return n + factorial_recursion(n-1)


print(factorial_recursion(5))


def find(n):
    s = 0
    length = len(n)
    for i in range(1, length):
        if n[s] < n[i]:
            s = i

    return n[s]


def find_recursion(n):
    length = len(n)
    if length == 1:
        return n[0]
    max_n_1 = find_recursion(n-1)
    if max_n_1 > n[length-1]:
        return max_n_1
    else:
        return n[length - 1]


def find_recursion1(a, n):
    if n == 1:
        return a[0]
    max_n_1 = find_recursion1(a, n-1)
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]


n = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]

print(find(n))
print(find_recursion1(n, len(n)))


def fibo(n):
    if n <= 1:
        return n
    s = fibo(n-1) + fibo(n-2)
    return s


print(fibo(5))
