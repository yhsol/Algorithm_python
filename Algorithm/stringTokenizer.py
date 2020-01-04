string = "asdfg"


def stringTokenizer(string):
    result = []

    for chr in string:
        result.append(chr)

    return result


result = stringTokenizer(string)
reverseResult = ''.join(reversed(result))
print(reverseResult)
