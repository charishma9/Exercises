def power(a,b):
    if b==1:
        return a
    if b!=1:
        return a*power(a,b-1)