def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1



print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 2"))