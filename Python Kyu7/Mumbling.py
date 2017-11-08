def accum(s):

    newlist = ""
    for i in range(len(s)):
        newlist += (s[i] * (i+1)) +"-"

    return newlist.title()[:-1]

#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))