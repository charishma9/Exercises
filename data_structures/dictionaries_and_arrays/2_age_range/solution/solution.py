def remove_ages(pdict,x,y):
    new ={}
    print(pdict)
    for i,j in pdict.items():
        if x<=j<=y:
            new[i]=j         
    return new

