str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(":")
print(ipos)

piece = str[ipos + 2:]
print(piece)
print(type(piece))

value = float(piece)
print(value)
print(type(value))
