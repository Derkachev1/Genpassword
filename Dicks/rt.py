a1 = "aretheyhere"
a2 = "yestheyarehere"
a3 = a1 + a2
lis = []
for i in a3:
    lis.append(i)
    lis.sort()
    g = set(lis)
    op = list(g)
    op.sort()
    re = " ".join(op)
    ret = re.replace(" ","")
print(ret)