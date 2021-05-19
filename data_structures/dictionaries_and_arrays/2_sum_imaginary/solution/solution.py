def sum_imaginary(ilst):
    x = 0
    y = 0
    for i in range(len(ilst)):
        x = x+ilst[i][0]
        y=y+ilst[i][1]
    return x,y
