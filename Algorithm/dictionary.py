def find_same_name(a):
    name_dict = {}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    print(name_dict)
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result


name = ["Tom", "Jerry", "Mike", "Tom"]
print("name: ", find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print("name2: ", find_same_name(name2))
