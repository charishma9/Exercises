def sum_tuples(tlst):
    n =[]
    for i in tlst:
        s = 0
        for j in range(len(i)):
            s = s+i[j]
        n.append(s)
    return n
        