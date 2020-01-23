
def find(n):
    length = len(n)
    s = set()
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if n[i] != n[j]:
                print(n[i], "-", a[j])

    return s


data = ["Tom", "Mike", "Jerry", "Tom", "Jerry"]

print(find(data))
