def find_ind_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)


def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ind_idx(result, value)
        result.insert(ins_idx, value)
    return result


def ins_sort_2(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


d = [2, 4, 5, 1, 3]
ins_sort_2(d)
print(d)
