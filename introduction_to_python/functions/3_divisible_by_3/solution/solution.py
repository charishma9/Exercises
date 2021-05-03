# Write your code here
def divisible_by_3(*args):
    y = []
    for x in args:
        if x%3==0:
            y.append(x)
    return y
