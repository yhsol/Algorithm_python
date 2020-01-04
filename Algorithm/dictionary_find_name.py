d = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}


def find_name(a, d):
    if a in d:
        return d[a]
    else:
        return "?"


print(find_name(39, d))
