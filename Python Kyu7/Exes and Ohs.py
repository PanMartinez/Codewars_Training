def xo(s):
    string = s.upper()
    xs = string.count("X")
    os = string.count("O")

    if xs == os:
        return True
    else:
        return False


print(xo('xo'))
print(xo('xo0'))
print(xo('xxxoo'))
