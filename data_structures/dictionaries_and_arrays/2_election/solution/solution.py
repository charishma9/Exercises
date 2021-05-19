def election_winner(clst):
    uni =[]
    dic ={}
    res = []
    for i in clst:
        if i not in uni:
            uni.append(i)
    for j in uni:
        c= clst.count(j)
        dic[j]=c
    nam = max(dic.items(), key = lambda x:x[1])
    for k,v in dic.items():
        if v == nam[1]:
            res.append(k)
    res.sort()
    return res[0]