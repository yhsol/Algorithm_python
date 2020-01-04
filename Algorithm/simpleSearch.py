arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]


def simpleSearch(arr, data):
    for i in range(0, len(arr)):
        if arr[i] == data:
            return i
    return -1


print(simpleSearch(arr, 8))
