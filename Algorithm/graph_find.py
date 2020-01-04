def graph_find(a, start):
    qu = []
    done = set()
    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in a[p]:
            if x not in done:
                qu.append(x)
                done.add(x)
                print(qu)


list = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

graph_find(list, 1)
print()
