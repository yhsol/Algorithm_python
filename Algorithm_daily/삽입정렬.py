def find(a, v):
    for i in range(0, len(a)):
        if v < a[i]:
            return i
    return len(a)


def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find(result, value)
        result.insert(ins_idx, value)
    return result


d = [2, 4, 5, 1, 3]
print(ins_sort(d))
