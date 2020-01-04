def palindrome(s):
    qu = []
    st = []

    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True


print(palindrome("Wow"))
print(palindrome("Madam, i'm Adam."))
print(palindrome("Madam, i am Adam."))


def appendalphabet(word):
    qu = []
    reversequ = []

    for x in word:
        if x is not None:
            qu.append(x)
            print(qu)
            print(reversed(qu))

    if qu == reversequ:
        return True
    else:
        return False


print(appendalphabet("wow"))
