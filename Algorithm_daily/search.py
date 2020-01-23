def search_list(a, x):
    n = len(a)
    s = []
    for i in range(0, n):
        if x == a[i]:
            s.append(i)
    return s


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))


def search_no(no, name, idx):
    n = len(no)

    for i in range(0, n):
        if idx == no[i]:
            return name[i]

    return "?"


no = [39, 14, 67, 105]
name = ["Justin", "John", "Mike", "Summer"]
print(search_no(no, name, 39))
